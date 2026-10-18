# HalpHvGetTscFrequency

- RVA: `0x0054C140`–`0x0054C16A` (길이 `42` bytes)
- VA: `0x000000014054C140`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `42/42` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0054C147` → [HalpHvIsFrequencyAvailable](HalpHvIsFrequencyAvailable_function_0054C2B4.md) (function, `0x0054C2B4`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0054C140  48 83 EC 28                     sub rsp, 0x28
0054C144  45 33 D2                        xor r10d, r10d
0054C147  E8 68 01 00 00                  call 0x14054c2b4
0054C14C  84 C0                           test al, al
0054C14E  74 11                           je 0x14054c161
0054C150  B9 22 00 00 40                  mov ecx, 0x40000022
0054C155  0F 32                           rdmsr
0054C157  48 C1 E2 20                     shl rdx, 0x20
0054C15B  48 0B C2                        or rax, rdx
0054C15E  4C 8B D0                        mov r10, rax
0054C161  49 8B C2                        mov rax, r10
0054C164  48 83 C4 28                     add rsp, 0x28
0054C168  C3                              ret
0054C169  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpHvGetTscFrequency(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    v_r10 = 0;
    result = HalpHvIsFrequencyAvailable(a1, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        a1 = 0x40000022ULL;
        a2 = (a2) << (32);
        result = (result) | (a2);
        v_r10 = result;
    }
    v_rsp = (v_rsp) + (40);
    return v_r10;
}
```

## 5. (Beta) C Style

```c
int64_t HalpHvGetTscFrequency(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    local_r10 = 0;
    result = HalpHvIsFrequencyAvailable(Arg1, Arg2, a3, a4);
    if ((uint8_t)(result) != 0) {
        Arg1 = 0x40000022ULL;
        Arg2 = (Arg2) << (32);
        result = (result) | (Arg2);
        local_r10 = result;
    }
    local_rsp = (local_rsp) + (40);
    return local_r10;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0054C140&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0054C140[BB_0054C140]
  bb_0054C150[BB_0054C150]
  bb_0054C161[BB_0054C161]
  bb_0054C169[BB_0054C169]
  bb_0054C140 -->|branch| bb_0054C161
  bb_0054C140 -->|fallthrough| bb_0054C150
  bb_0054C150 -->|flow| bb_0054C161
```
