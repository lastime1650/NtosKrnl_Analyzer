# HsaDeleteDevice

- RVA: `0x00573C70`–`0x00573C9F` (길이 `47` bytes)
- VA: `0x0000000140573C70`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `15`개 명령, `47/47` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00573C82` → [HsaFreePasidTables](HsaFreePasidTables_function_0057401C.md) (function, `0x0057401C`)
- `0x00573C8B` → [ExtEnvFreeMemory](../56/ExtEnvFreeMemory_function_00561320.md) (function, `0x00561320`)
- `0x00573C93` → [ExtEnvFreeMemory](../56/ExtEnvFreeMemory_function_00561320.md) (function, `0x00561320`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00573C70  40 53                           push rbx
00573C72  48 83 EC 20                     sub rsp, 0x20
00573C76  48 8B DA                        mov rbx, rdx
00573C79  48 8B 52 30                     mov rdx, qword ptr [rdx + 0x30]
00573C7D  48 85 D2                        test rdx, rdx
00573C80  74 05                           je 0x140573c87
00573C82  E8 95 03 00 00                  call 0x14057401c
00573C87  48 8B 53 28                     mov rdx, qword ptr [rbx + 0x28]
00573C8B  E8 90 D6 FE FF                  call 0x140561320
00573C90  48 8B D3                        mov rdx, rbx
00573C93  E8 88 D6 FE FF                  call 0x140561320
00573C98  48 83 C4 20                     add rsp, 0x20
00573C9C  5B                              pop rbx
00573C9D  C3                              ret
00573C9E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HsaDeleteDevice(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if (*(unsigned __int64 *)(a2 + 48) != 0) {
        result = HsaFreePasidTables(a1, *(unsigned __int64 *)(a2 + 48), a3, a4);
    }
    result = ExtEnvFreeMemory(a1, *(unsigned __int64 *)(a2 + 40), a3, a4);
    result = ExtEnvFreeMemory(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HsaDeleteDevice(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if (*(uint64_t *)(arg2 + 0x30) != 0) {
        result = HsaFreePasidTables(Arg1, *(uint64_t *)(arg2 + 0x30), a3, a4);
    }
    result = ExtEnvFreeMemory(Arg1, *(uint64_t *)(arg2 + 0x28), a3, a4);
    result = ExtEnvFreeMemory(Arg1, Arg2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x28` | `64` | `R` |
| `Arg2` | `+ 0x30` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00573C70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00573C70[BB_00573C70]
  bb_00573C82[BB_00573C82]
  bb_00573C87[BB_00573C87]
  bb_00573C9E[BB_00573C9E]
  bb_00573C70 -->|branch| bb_00573C87
  bb_00573C70 -->|fallthrough| bb_00573C82
  bb_00573C82 -->|flow| bb_00573C87
```
