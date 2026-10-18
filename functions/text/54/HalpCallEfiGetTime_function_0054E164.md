# HalpCallEfiGetTime

- RVA: `0x0054E164`–`0x0054E17F` (길이 `27` bytes)
- VA: `0x000000014054E164`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0054E174` → `indirect target` (indirect, 간접 대상)

### Direct callers
- [HalEfiGetTime](HalEfiGetTime_function_0054DC6C.md) at `0x0054DCDE`
- [HalEfiSetTime](HalEfiSetTime_function_0054DE84.md) at `0x0054DF03`

### Static image references
- `0x0054E168` → RVA `0x01200010` (`CFGRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0054E164  48 83 EC 28                     sub rsp, 0x28
0054E168  48 8B 05 A1 1E CB 00            mov rax, qword ptr [rip + 0xcb1ea1]
0054E16F  33 D2                           xor edx, edx
0054E171  48 8B 00                        mov rax, qword ptr [rax]
0054E174  FF D0                           call rax
0054E176  0F 1F 00                        nop dword ptr [rax]
0054E179  48 83 C4 28                     add rsp, 0x28
0054E17D  C3                              ret
0054E17E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpCallEfiGetTime(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a2 = 0;
    result = kernel_indirect_call(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalpCallEfiGetTime(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg2 = 0;
    result = kernel_indirect_call(Arg1, Arg2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0054E164&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0054E164[BB_0054E164]
  bb_0054E17E[BB_0054E17E]
```
