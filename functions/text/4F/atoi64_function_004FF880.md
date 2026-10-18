# atoi64

- RVA: `0x004FF880`–`0x004FF89E` (길이 `30` bytes)
- VA: `0x00000001404FF880`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `11`개 명령, `30/30` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004FF893` → [strtoi64](strtoi64_function_004FF618.md) (function, `0x004FF618`)

### Direct callers
- [KiMatchLoadOption](../../pagelk/B6/KiMatchLoadOption_function_00B67598.md) at `0x00B675BF`
- [RamdiskStart](../../init/C6/RamdiskStart_function_00C6EF68.md) at `0x00C6F13D`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004FF880  48 83 EC 28                     sub rsp, 0x28
004FF884  48 85 C9                        test rcx, rcx
004FF887  75 04                           jne 0x1404ff88d
004FF889  33 C0                           xor eax, eax
004FF88B  EB 0B                           jmp 0x1404ff898
004FF88D  33 D2                           xor edx, edx
004FF88F  44 8D 42 0A                     lea r8d, [rdx + 0xa]
004FF893  E8 80 FD FF FF                  call 0x1404ff618
004FF898  48 83 C4 28                     add rsp, 0x28
004FF89C  C3                              ret
004FF89D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall atoi64(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a1 != 0) goto loc_004FF88D;
    result = 0;
    goto loc_004FF898;
loc_004FF88D:
    a2 = 0;
    result = strtoi64(a1, a2, a2 + 10, a4);
loc_004FF898:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t atoi64(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg1 != 0) goto loc_004FF88D;
    result = 0;
    goto loc_004FF898;
loc_004FF88D:
    Arg2 = 0;
    result = strtoi64(Arg1, Arg2, Arg2 + 10, a4);
loc_004FF898:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004FF880&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004FF880[BB_004FF880]
  bb_004FF889[BB_004FF889]
  bb_004FF88D[BB_004FF88D]
  bb_004FF898[BB_004FF898]
  bb_004FF89D[BB_004FF89D]
  bb_004FF880 -->|branch| bb_004FF88D
  bb_004FF880 -->|fallthrough| bb_004FF889
  bb_004FF889 -->|branch| bb_004FF898
  bb_004FF88D -->|flow| bb_004FF898
```
