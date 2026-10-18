# NtCreateFile

- RVA: `0x008AB210`–`0x008AB292` (길이 `130` bytes)
- VA: `0x00000001408AB210`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007F69C`
- 디코드: `25`개 명령, `130/130` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008AB284` → [IopCreateFile](IopCreateFile_function_008AB298.md) (function, `0x008AB298`)

### Direct callers
- [DifNtCreateFileWrapper](../../text/63/DifNtCreateFileWrapper_function_00637260.md) at `0x006373BE`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008AB210  48 81 EC 88 00 00 00            sub rsp, 0x88
008AB217  33 C0                           xor eax, eax
008AB219  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
008AB21E  C7 44 24 70 20 00 00 00         mov dword ptr [rsp + 0x70], 0x20
008AB226  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
008AB22A  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
008AB22F  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
008AB233  8B 84 24 E0 00 00 00            mov eax, dword ptr [rsp + 0xe0]
008AB23A  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
008AB23E  48 8B 84 24 D8 00 00 00         mov rax, qword ptr [rsp + 0xd8]
008AB246  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
008AB24B  8B 84 24 D0 00 00 00            mov eax, dword ptr [rsp + 0xd0]
008AB252  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
008AB256  8B 84 24 C8 00 00 00            mov eax, dword ptr [rsp + 0xc8]
008AB25D  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
008AB261  8B 84 24 C0 00 00 00            mov eax, dword ptr [rsp + 0xc0]
008AB268  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
008AB26C  8B 84 24 B8 00 00 00            mov eax, dword ptr [rsp + 0xb8]
008AB273  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
008AB277  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
008AB27F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008AB284  E8 0F 00 00 00                  call 0x1408ab298
008AB289  48 81 C4 88 00 00 00            add rsp, 0x88
008AB290  C3                              ret
008AB291  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtCreateFile(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, unsigned int a6, unsigned int a7, unsigned int a8, unsigned int a9, __int64 a10, unsigned int a11)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned int v_stack_m18;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
    unsigned int v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m48;
    unsigned int v_stack_m50;
    unsigned int v_stack_m58;
    unsigned int v_stack_m60;
    unsigned __int64 v_stack_m68;

    v_rsp = (v_rsp) - (136);
    result = 0;
    v_stack_m10 = 0;
    v_stack_m18 = 32;
    v_stack_m20 = 0;
    v_stack_m28 = 0;
    v_stack_m30 = 0;
    v_stack_m38 = (unsigned int)((unsigned int)(a11));
    v_stack_m40 = a10;
    v_stack_m48 = (unsigned int)((unsigned int)(a9));
    v_stack_m50 = (unsigned int)((unsigned int)(a8));
    v_stack_m58 = (unsigned int)((unsigned int)(a7));
    v_stack_m60 = (unsigned int)((unsigned int)(a6));
    v_stack_m68 = a5;
    result = IopCreateFile(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (136);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t NtCreateFile(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, uint32_t Arg6, uint32_t Arg7, uint32_t Arg8, uint32_t Arg9, int64_t Arg10, uint32_t Arg11)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint32_t v_stack_m18;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
    uint32_t v_stack_m38;
    uint64_t v_stack_m40;
    uint32_t v_stack_m48;
    uint32_t v_stack_m50;
    uint32_t v_stack_m58;
    uint32_t v_stack_m60;
    uint64_t v_stack_m68;

    local_rsp = (local_rsp) - (136);
    result = 0;
    v_stack_m10 = 0;
    v_stack_m18 = 32;
    v_stack_m20 = 0;
    v_stack_m28 = 0;
    v_stack_m30 = 0;
    v_stack_m38 = (uint32_t)((uint32_t)(Arg11));
    v_stack_m40 = Arg10;
    v_stack_m48 = (uint32_t)((uint32_t)(Arg9));
    v_stack_m50 = (uint32_t)((uint32_t)(Arg8));
    v_stack_m58 = (uint32_t)((uint32_t)(Arg7));
    v_stack_m60 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m68 = Arg5;
    result = IopCreateFile(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (136);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008AB210&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008AB210[BB_008AB210]
  bb_008AB291[BB_008AB291]
```
