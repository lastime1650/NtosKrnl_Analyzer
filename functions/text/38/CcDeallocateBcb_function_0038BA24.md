# CcDeallocateBcb

- RVA: `0x0038BA24`–`0x0038BA51` (길이 `45` bytes)
- VA: `0x000000014038BA24`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `15`개 명령, `45/45` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0038BA3B` → [ExDeleteResourceLite](ExDeleteResourceLite_function_0038BA60.md) (function, `0x0038BA60`)
- `0x0038BA45` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [CcUnpinFileDataEx](../35/CcUnpinFileDataEx_function_00359DEC.md) at `0x0035A088`
- [CcDeleteBcbs](CcDeleteBcbs_function_00389BF0.md) at `0x00389D09`
- [CcDeleteMbcb](CcDeleteMbcb_function_0038C088.md) at `0x0038C152`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0038BA45` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0038BA24  40 53                           push rbx
0038BA26  48 83 EC 20                     sub rsp, 0x20
0038BA2A  B8 FD 02 00 00                  mov eax, 0x2fd
0038BA2F  48 8B D9                        mov rbx, rcx
0038BA32  66 39 01                        cmp word ptr [rcx], ax
0038BA35  75 09                           jne 0x14038ba40
0038BA37  48 83 C1 48                     add rcx, 0x48
0038BA3B  E8 20 00 00 00                  call 0x14038ba60
0038BA40  33 D2                           xor edx, edx
0038BA42  48 8B CB                        mov rcx, rbx
0038BA45  E8 26 6E 7F 00                  call 0x140b82870
0038BA4A  48 83 C4 20                     add rsp, 0x20
0038BA4E  5B                              pop rbx
0038BA4F  C3                              ret
0038BA50  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CcDeallocateBcb(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = 765;
    if ((*(unsigned __int16 *)(a1)) == 765) {
        a1 = (a1) + (72);
        result = ExDeleteResourceLite(a1, a2, a3, a4);
    }
    a2 = 0;
    result = ExFreePoolWithTag(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CcDeallocateBcb(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = 765;
    if ((*(uint16_t *)(arg1)) == 765) {
        Arg1 = (Arg1) + (72);
        result = ExDeleteResourceLite(Arg1, Arg2, a3, a4);
    }
    Arg2 = 0;
    result = ExFreePoolWithTag(Arg1, Arg2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `16` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0038BA24&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0038BA24[BB_0038BA24]
  bb_0038BA37[BB_0038BA37]
  bb_0038BA40[BB_0038BA40]
  bb_0038BA50[BB_0038BA50]
  bb_0038BA24 -->|branch| bb_0038BA40
  bb_0038BA24 -->|fallthrough| bb_0038BA37
  bb_0038BA37 -->|flow| bb_0038BA40
```
