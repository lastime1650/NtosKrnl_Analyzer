# LdrpKrnGetDataTableEntry

- RVA: `0x004563B4`–`0x004563DF` (길이 `43` bytes)
- VA: `0x00000001404563B4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007EE6C`
- 디코드: `16`개 명령, `43/43` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004563BC` → [MiLockLoadedDataTableEntry](../2A/MiLockLoadedDataTableEntry_function_002A38F4.md) (function, `0x002A38F4`)
- `0x004563D8` → [MiUnlockLoadedDataTableEntry](../2A/MiUnlockLoadedDataTableEntry_function_002A385C.md) (function, `0x002A385C`)

### Direct callers
- [LdrLoadAlternateResourceModuleEx](LdrLoadAlternateResourceModuleEx_function_004557CC.md) at `0x004558B8`
- [LdrpGetImageSize](LdrpGetImageSize_function_004562F0.md) at `0x0045634E`
- [LdrpResGetMappingSize](../../page/99/LdrpResGetMappingSize_function_00991614.md) at `0x00991734`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004563B4  40 53                           push rbx
004563B6  48 83 EC 20                     sub rsp, 0x20
004563BA  33 D2                           xor edx, edx
004563BC  E8 33 D5 E4 FF                  call 0x1402a38f4
004563C1  48 8B D8                        mov rbx, rax
004563C4  48 85 C0                        test rax, rax
004563C7  75 0A                           jne 0x1404563d3
004563C9  48 8B C3                        mov rax, rbx
004563CC  48 83 C4 20                     add rsp, 0x20
004563D0  5B                              pop rbx
004563D1  C3                              ret
004563D2  CC                              int3
004563D3  33 D2                           xor edx, edx
004563D5  48 8B CB                        mov rcx, rbx
004563D8  E8 7F D4 E4 FF                  call 0x1402a385c
004563DD  EB EA                           jmp 0x1404563c9
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall LdrpKrnGetDataTableEntry(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a2 = 0;
    result = MiLockLoadedDataTableEntry(a1, a2, a3, a4);
    if (result != 0) goto loc_004563D3;
loc_004563C9:
    v_rsp = (v_rsp) + (32);
    return result;
loc_004563D3:
    a2 = 0;
    result = MiUnlockLoadedDataTableEntry(result, a2, a3, a4);
    goto loc_004563C9;
}
```

## 5. (Beta) C Style

```c
int64_t LdrpKrnGetDataTableEntry(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    Arg2 = 0;
    result = MiLockLoadedDataTableEntry(Arg1, Arg2, a3, a4);
    if (result != 0) goto loc_004563D3;
loc_004563C9:
    local_rsp = (local_rsp) + (32);
    return result;
loc_004563D3:
    Arg2 = 0;
    result = MiUnlockLoadedDataTableEntry(result, Arg2, a3, a4);
    goto loc_004563C9;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004563B4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004563B4[BB_004563B4]
  bb_004563C9[BB_004563C9]
  bb_004563D2[BB_004563D2]
  bb_004563D3[BB_004563D3]
  bb_004563B4 -->|branch| bb_004563D3
  bb_004563B4 -->|fallthrough| bb_004563C9
  bb_004563D2 -->|flow| bb_004563D3
  bb_004563D3 -->|branch| bb_004563C9
```
