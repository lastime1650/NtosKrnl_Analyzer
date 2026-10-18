# ObpDeleteSymbolicLink

- RVA: `0x00A78E20`–`0x00A78E4C` (길이 `44` bytes)
- VA: `0x0000000140A78E20`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `16`개 명령, `44/44` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A78E3B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00A78E3B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A78E20  40 53                           push rbx
00A78E22  48 83 EC 20                     sub rsp, 0x20
00A78E26  8B 41 1C                        mov eax, dword ptr [rcx + 0x1c]
00A78E29  48 8B D9                        mov rbx, rcx
00A78E2C  A8 10                           test al, 0x10
00A78E2E  75 10                           jne 0x140a78e40
00A78E30  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
00A78E34  48 85 C9                        test rcx, rcx
00A78E37  74 07                           je 0x140a78e40
00A78E39  33 D2                           xor edx, edx
00A78E3B  E8 30 9A 10 00                  call 0x140b82870
00A78E40  48 83 63 10 00                  and qword ptr [rbx + 0x10], 0
00A78E45  48 83 C4 20                     add rsp, 0x20
00A78E49  5B                              pop rbx
00A78E4A  C3                              ret
00A78E4B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ObpDeleteSymbolicLink(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 28)))) & (16)) != 0) goto loc_00A78E40;
    result = (unsigned int)(*(unsigned int *)(a1 + 28));
    if (*(unsigned __int64 *)(a1 + 16) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(a1 + 16), a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ObpDeleteSymbolicLink(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1C)))) & (16)) != 0) goto loc_00A78E40;
    result = (uint32_t)(*(uint32_t *)(arg1 + 0x1C));
    if (*(uint64_t *)(arg1 + 0x10) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(arg1 + 0x10), Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R/W` |
| `Arg1` | `+ 0x1C` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A78E20&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A78E20[BB_00A78E20]
  bb_00A78E30[BB_00A78E30]
  bb_00A78E39[BB_00A78E39]
  bb_00A78E40[BB_00A78E40]
  bb_00A78E4B[BB_00A78E4B]
  bb_00A78E20 -->|branch| bb_00A78E40
  bb_00A78E20 -->|fallthrough| bb_00A78E30
  bb_00A78E30 -->|branch| bb_00A78E40
  bb_00A78E30 -->|fallthrough| bb_00A78E39
  bb_00A78E39 -->|flow| bb_00A78E40
```
