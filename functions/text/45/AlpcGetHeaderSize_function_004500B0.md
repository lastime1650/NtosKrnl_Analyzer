# AlpcGetHeaderSize

- RVA: `0x004500B0`–`0x00450100` (길이 `80` bytes)
- VA: `0x00000001404500B0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `25`개 명령, `80/80` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [AlpcGetMessageAttribute](AlpcGetMessageAttribute_function_00450010.md) at `0x0045002E`
- [AlpcInitializeMessageAttribute](AlpcInitializeMessageAttribute_function_00450050.md) at `0x0045006F`
- [AlpcpInitializeCompletionList](../../page/A1/AlpcpInitializeCompletionList_function_00A1A6D0.md) at `0x00A1ABB5`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004500B0  44 8B C1                        mov r8d, ecx
004500B3  8B D1                           mov edx, ecx
004500B5  C1 FA 1F                        sar edx, 0x1f
004500B8  83 E2 18                        and edx, 0x18
004500BB  83 C2 08                        add edx, 8
004500BE  0F BA E1 1E                     bt ecx, 0x1e
004500C2  8D 42 20                        lea eax, [rdx + 0x20]
004500C5  0F 43 C2                        cmovae eax, edx
004500C8  0F BA E1 1D                     bt ecx, 0x1d
004500CC  8D 48 20                        lea ecx, [rax + 0x20]
004500CF  0F 43 C8                        cmovae ecx, eax
004500D2  41 0F BA E0 1C                  bt r8d, 0x1c
004500D7  8D 41 18                        lea eax, [rcx + 0x18]
004500DA  0F 43 C1                        cmovae eax, ecx
004500DD  41 0F BA E0 1B                  bt r8d, 0x1b
004500E2  8D 48 18                        lea ecx, [rax + 0x18]
004500E5  0F 43 C8                        cmovae ecx, eax
004500E8  41 0F BA E0 1A                  bt r8d, 0x1a
004500ED  8D 51 08                        lea edx, [rcx + 8]
004500F0  0F 43 D1                        cmovae edx, ecx
004500F3  41 0F BA E0 19                  bt r8d, 0x19
004500F8  8D 42 08                        lea eax, [rdx + 8]
004500FB  0F 43 C2                        cmovae eax, edx
004500FE  C3                              ret
004500FF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AlpcGetHeaderSize(int a1)
{
    __int64 result;

    a2 = (unsigned int)(((unsigned int)(a1)) >> (31));
    a2 = (unsigned int)((a2) & (24));
    a2 = (unsigned int)((a2) + (8));
    result = a2 + 32;
    if (condition_is_above_or_equal) { result = (unsigned int)(a2); }
    a1 = result + 32;
    if (condition_is_above_or_equal) { a1 = (unsigned int)(result); }
    result = a1 + 24;
    if (condition_is_above_or_equal) { result = a1; }
    a1 = result + 24;
    if (condition_is_above_or_equal) { a1 = (unsigned int)(result); }
    a2 = a1 + 8;
    if (condition_is_above_or_equal) { a2 = a1; }
    result = a2 + 8;
    if (condition_is_above_or_equal) { result = (unsigned int)(a2); }
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t AlpcGetHeaderSize(int32_t Arg1)
{
    int64_t result;

    a2 = (uint32_t)(((uint32_t)(Arg1)) >> (31));
    a2 = (uint32_t)((a2) & (24));
    a2 = (uint32_t)((a2) + (8));
    result = a2 + 32;
    if (condition_is_above_or_equal) { result = (uint32_t)(a2); }
    Arg1 = result + 32;
    if (condition_is_above_or_equal) { Arg1 = (uint32_t)(result); }
    result = Arg1 + 24;
    if (condition_is_above_or_equal) { result = Arg1; }
    Arg1 = result + 24;
    if (condition_is_above_or_equal) { Arg1 = (uint32_t)(result); }
    a2 = Arg1 + 8;
    if (condition_is_above_or_equal) { a2 = Arg1; }
    result = a2 + 8;
    if (condition_is_above_or_equal) { result = (uint32_t)(a2); }
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004500B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004500B0[BB_004500B0]
  bb_004500FF[BB_004500FF]
```
