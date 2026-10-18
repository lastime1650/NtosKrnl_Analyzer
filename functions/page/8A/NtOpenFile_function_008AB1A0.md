# NtOpenFile

- RVA: `0x008AB1A0`–`0x008AB201` (길이 `97` bytes)
- VA: `0x00000001408AB1A0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007F678`
- 디코드: `21`개 명령, `97/97` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008AB1F3` → [IopCreateFile](IopCreateFile_function_008AB298.md) (function, `0x008AB298`)

### Direct callers
- [DifNtOpenFileWrapper](../../text/63/DifNtOpenFileWrapper_function_00637980.md) at `0x00637A95`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008AB1A0  4C 8B DC                        mov r11, rsp
008AB1A3  48 81 EC 88 00 00 00            sub rsp, 0x88
008AB1AA  8B 84 24 B8 00 00 00            mov eax, dword ptr [rsp + 0xb8]
008AB1B1  45 33 D2                        xor r10d, r10d
008AB1B4  4D 89 53 F0                     mov qword ptr [r11 - 0x10], r10
008AB1B8  C7 44 24 70 20 00 00 00         mov dword ptr [rsp + 0x70], 0x20
008AB1C0  45 89 53 E0                     mov dword ptr [r11 - 0x20], r10d
008AB1C4  4D 89 53 D8                     mov qword ptr [r11 - 0x28], r10
008AB1C8  45 89 53 D0                     mov dword ptr [r11 - 0x30], r10d
008AB1CC  45 89 53 C8                     mov dword ptr [r11 - 0x38], r10d
008AB1D0  4D 89 53 C0                     mov qword ptr [r11 - 0x40], r10
008AB1D4  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
008AB1D8  8B 84 24 B0 00 00 00            mov eax, dword ptr [rsp + 0xb0]
008AB1DF  C7 44 24 38 01 00 00 00         mov dword ptr [rsp + 0x38], 1
008AB1E7  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
008AB1EB  45 89 53 A0                     mov dword ptr [r11 - 0x60], r10d
008AB1EF  4D 89 53 98                     mov qword ptr [r11 - 0x68], r10
008AB1F3  E8 A0 00 00 00                  call 0x1408ab298
008AB1F8  48 81 C4 88 00 00 00            add rsp, 0x88
008AB1FF  C3                              ret
008AB200  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtOpenFile(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, unsigned int a6)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_rsp;
    unsigned int v_stack_m18;
    unsigned int v_stack_m48;
    unsigned int v_stack_m50;
    unsigned int v_stack_m58;

    v_rsp = (v_rsp) - (136);
    v_r10 = 0;
    *(unsigned __int64 *)(v_rsp - 16) = 0;
    v_stack_m18 = 32;
    *(unsigned int *)(v_rsp - 32) = 0;
    *(unsigned __int64 *)(v_rsp - 40) = 0;
    *(unsigned int *)(v_rsp - 48) = 0;
    *(unsigned int *)(v_rsp - 56) = 0;
    *(unsigned __int64 *)(v_rsp - 64) = 0;
    v_stack_m48 = (unsigned int)((unsigned int)(a6));
    v_stack_m50 = 1;
    v_stack_m58 = (unsigned int)((unsigned int)(a5));
    *(unsigned int *)(v_rsp - 96) = 0;
    *(unsigned __int64 *)(v_rsp - 104) = 0;
    result = IopCreateFile(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (136);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t NtOpenFile(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5, uint32_t Arg6)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_rsp;
    uint32_t v_stack_m18;
    uint32_t v_stack_m48;
    uint32_t v_stack_m50;
    uint32_t v_stack_m58;

    local_rsp = (local_rsp) - (136);
    local_r10 = 0;
    *(uint64_t *)(local_rsp - 0x10) = 0;
    v_stack_m18 = 32;
    *(uint32_t *)(local_rsp - 0x20) = 0;
    *(uint64_t *)(local_rsp - 0x28) = 0;
    *(uint32_t *)(local_rsp - 0x30) = 0;
    *(uint32_t *)(local_rsp - 0x38) = 0;
    *(uint64_t *)(local_rsp - 0x40) = 0;
    v_stack_m48 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m50 = 1;
    v_stack_m58 = (uint32_t)((uint32_t)(Arg5));
    *(uint32_t *)(local_rsp - 0x60) = 0;
    *(uint64_t *)(local_rsp - 0x68) = 0;
    result = IopCreateFile(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (136);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008AB1A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008AB1A0[BB_008AB1A0]
  bb_008AB200[BB_008AB200]
```
