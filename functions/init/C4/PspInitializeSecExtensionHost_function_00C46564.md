# PspInitializeSecExtensionHost

- RVA: `0x00C46564`–`0x00C465CE` (길이 `106` bytes)
- VA: `0x0000000140C46564`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009EAB4`
- 디코드: `26`개 명령, `106/106` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00C465B2` → [ExRegisterHost](../../page/7D/ExRegisterHost_function_007D06CC.md) (function, `0x007D06CC`)

### Direct callers
- [PspInitPhase1](PspInitPhase1_function_00C453B8.md) at `0x00C45428`

### Static image references
- `0x00C46571` → RVA `0x000087C8` (`.rdata`; read)
- `0x00C465A3` → RVA `0x00E67AC0` (`.data`; read)
- `0x00C465BB` → RVA `0x00E67AC0` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00C465B2` → [ExRegisterHost](../../page/7D/ExRegisterHost_function_007D06CC.md) (`INIT` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C46564  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00C46569  55                              push rbp
00C4656A  48 8B EC                        mov rbp, rsp
00C4656D  48 83 EC 60                     sub rsp, 0x60
00C46571  48 8D 05 50 22 3C FF            lea rax, [rip - 0xc3ddb0]
00C46578  48 C7 45 D0 0E 00 01 00         mov qword ptr [rbp - 0x30], 0x1000e
00C46580  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
00C46584  4C 8D 45 D0                     lea r8, [rbp - 0x30]
00C46588  48 8D 45 C0                     lea rax, [rbp - 0x40]
00C4658C  C7 45 C0 01 00 00 00            mov dword ptr [rbp - 0x40], 1
00C46593  0F 57 C0                        xorps xmm0, xmm0
00C46596  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
00C4659A  33 DB                           xor ebx, ebx
00C4659C  C7 45 E0 00 02 00 00            mov dword ptr [rbp - 0x20], 0x200
00C465A3  48 8D 0D 16 15 22 00            lea rcx, [rip + 0x221516]
00C465AA  89 5D F4                        mov dword ptr [rbp - 0xc], ebx
00C465AD  F3 0F 7F 45 E4                  movdqu xmmword ptr [rbp - 0x1c], xmm0
00C465B2  E8 15 A1 B8 FF                  call 0x1407d06cc
00C465B7  85 C0                           test eax, eax
00C465B9  79 07                           jns 0x140c465c2
00C465BB  48 89 1D FE 14 22 00            mov qword ptr [rip + 0x2214fe], rbx
00C465C2  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
00C465C7  48 83 C4 60                     add rsp, 0x60
00C465CB  5D                              pop rbp
00C465CC  C3                              ret
00C465CD  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspInitializeSecExtensionHost(void)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned int v_stack_m14;
    unsigned __int64 v_stack_m24;
    unsigned int v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (96);
    v_stack_m38 = 0x1000EULL;
    v_stack_m40 = v_rip - 12836272;
    v_stack_m48 = 1;
    v_stack_m30 = v_stack_m48;
    v_rbx = 0;
    v_stack_m28 = 512;
    v_stack_m14 = 0;
    v_stack_m24 = v_xmm0;
    result = ExRegisterHost(v_rip + 2233622, a2, v_stack_m38, a4);
    if (sign_flag) {
        *(unsigned __int64 *)(v_rip + 2233598) = 0;
    }
    v_rsp = (v_rsp) + (96);
    return result;
}
```

## 5. (Beta) C Style

```c
void PspInitializeSecExtensionHost(void)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint32_t v_stack_m14;
    uint64_t v_stack_m24;
    uint32_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (96);
    v_stack_m38 = 0x1000EULL;
    v_stack_m40 = v_rip - 12836272;
    v_stack_m48 = 1;
    v_stack_m30 = v_stack_m48;
    local_rbx = 0;
    v_stack_m28 = 512;
    v_stack_m14 = 0;
    v_stack_m24 = v_xmm0;
    result = ExRegisterHost(v_rip + 2233622, a2, v_stack_m38, a4);
    if (sign_flag) {
        *(uint64_t *)(v_rip + 0x2214FE) = 0;
    }
    local_rsp = (local_rsp) + (96);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C46564&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C46564[BB_00C46564]
  bb_00C465BB[BB_00C465BB]
  bb_00C465C2[BB_00C465C2]
  bb_00C465CD[BB_00C465CD]
  bb_00C46564 -->|branch| bb_00C465C2
  bb_00C46564 -->|fallthrough| bb_00C465BB
  bb_00C465BB -->|flow| bb_00C465C2
```
