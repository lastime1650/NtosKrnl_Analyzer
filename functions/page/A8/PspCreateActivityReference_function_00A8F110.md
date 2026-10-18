# PspCreateActivityReference

- RVA: `0x00A8F110`–`0x00A8F1FA` (길이 `234` bytes)
- VA: `0x0000000140A8F110`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B8BD4`
- 디코드: `57`개 명령, `234/234` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00A8F19A` → [ObCreateObjectEx](../89/ObCreateObjectEx_function_0089B1E0.md) (function, `0x0089B1E0`)
- `0x00A8F1CD` → [PsChargeProcessWakeCounter](../88/PsChargeProcessWakeCounter_function_0088BCD0.md) (function, `0x0088BCD0`)
- `0x00A8F1F3` → [ObInsertObjectEx](../8B/ObInsertObjectEx_function_008B97A0.md) (function, `0x008B97A0`)

### Direct callers
- [NtAcquireProcessActivityReference](NtAcquireProcessActivityReference_function_00A8EFF0.md) at `0x00A8F08F`

### Static image references
- `0x00A8F13F` → RVA `0x00FC72D8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A8F110  4C 8B DC                        mov r11, rsp
00A8F113  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00A8F117  49 89 73 10                     mov qword ptr [r11 + 0x10], rsi
00A8F11B  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
00A8F11F  55                              push rbp
00A8F120  48 8B EC                        mov rbp, rsp
00A8F123  48 81 EC 80 00 00 00            sub rsp, 0x80
00A8F12A  49 83 63 C0 00                  and qword ptr [r11 - 0x40], 0
00A8F12F  4C 8D 45 D0                     lea r8, [rbp - 0x30]
00A8F133  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A8F13C  48 8B FA                        mov rdi, rdx
00A8F13F  48 8B 15 92 81 53 00            mov rdx, qword ptr [rip + 0x538192]
00A8F146  48 8B F1                        mov rsi, rcx
00A8F149  83 65 EC 00                     and dword ptr [rbp - 0x14], 0
00A8F14D  0F 57 C0                        xorps xmm0, xmm0
00A8F150  48 83 65 20 00                  and qword ptr [rbp + 0x20], 0
00A8F155  33 C9                           xor ecx, ecx
00A8F157  44 8A 88 32 02 00 00            mov r9b, byte ptr [rax + 0x232]
00A8F15E  48 8D 45 20                     lea rax, [rbp + 0x20]
00A8F162  48 83 65 D8 00                  and qword ptr [rbp - 0x28], 0
00A8F167  48 83 65 E0 00                  and qword ptr [rbp - 0x20], 0
00A8F16C  49 89 43 B8                     mov qword ptr [r11 - 0x48], rax
00A8F170  B8 08 00 00 00                  mov eax, 8
00A8F175  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00A8F179  83 64 24 30 00                  and dword ptr [rsp + 0x30], 0
00A8F17E  48 C7 45 D0 30 00 00 00         mov qword ptr [rbp - 0x30], 0x30
00A8F186  83 65 D4 00                     and dword ptr [rbp - 0x2c], 0
00A8F18A  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00A8F18E  C7 45 E8 20 00 00 00            mov dword ptr [rbp - 0x18], 0x20
00A8F195  F3 0F 7F 45 F0                  movdqu xmmword ptr [rbp - 0x10], xmm0
00A8F19A  E8 41 C0 E0 FF                  call 0x14089b1e0
00A8F19F  85 C0                           test eax, eax
00A8F1A1  79 1A                           jns 0x140a8f1bd
00A8F1A3  4C 8D 9C 24 80 00 00 00         lea r11, [rsp + 0x80]
00A8F1AB  49 8B 5B 10                     mov rbx, qword ptr [r11 + 0x10]
00A8F1AF  49 8B 73 18                     mov rsi, qword ptr [r11 + 0x18]
00A8F1B3  49 8B 7B 28                     mov rdi, qword ptr [r11 + 0x28]
00A8F1B7  49 8B E3                        mov rsp, r11
00A8F1BA  5D                              pop rbp
00A8F1BB  C3                              ret
00A8F1BC  CC                              int3
00A8F1BD  48 8B 5D 20                     mov rbx, qword ptr [rbp + 0x20]
00A8F1C1  33 D2                           xor edx, edx
00A8F1C3  4C 8B CB                        mov r9, rbx
00A8F1C6  48 8B CE                        mov rcx, rsi
00A8F1C9  44 8D 42 05                     lea r8d, [rdx + 5]
00A8F1CD  E8 FE CA DF FF                  call 0x14088bcd0
00A8F1D2  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00A8F1D7  45 33 C9                        xor r9d, r9d
00A8F1DA  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
00A8F1E0  33 D2                           xor edx, edx
00A8F1E2  83 64 24 20 00                  and dword ptr [rsp + 0x20], 0
00A8F1E7  41 B8 00 00 0F 00               mov r8d, 0xf0000
00A8F1ED  48 8B CB                        mov rcx, rbx
00A8F1F0  48 89 03                        mov qword ptr [rbx], rax
00A8F1F3  E8 A8 A5 E2 FF                  call 0x1408b97a0
00A8F1F8  EB A9                           jmp 0x140a8f1a3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspCreateActivityReference(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned int v_stack_m34;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m50;
    unsigned int v_stack_m58;
    unsigned int v_stack_m60;
    unsigned __int64 v_stack_m8;
    unsigned __int64 v_stack_p18;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (128);
    a1 = 0;
    *(unsigned __int64 *)(v_rsp - 72) = v_stack_p18;
    v_stack_m50 = 8;
    v_stack_m38 = 48;
    v_stack_m60 = 8;
    v_stack_m20 = 32;
    v_stack_m18 = v_xmm0;
    result = ObCreateObjectEx(a1, *(unsigned __int64 *)(v_rip + 5472658), v_stack_m38, *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if (!sign_flag) goto loc_00A8F1BD;
loc_00A8F1A3:
    return result;
loc_00A8F1BD:
    a2 = 0;
    result = PsChargeProcessWakeCounter(*(unsigned __int64 *)(v_stack_m8 + 24), a2, a2 + 5, v_stack_p18);
    v_stack_m50 = *(unsigned __int64 *)(v_stack_m8 + 40);
    a4 = 0;
    a2 = 0;
    *(unsigned __int64 *)(v_stack_p18) = result;
    result = ObInsertObjectEx(v_stack_p18, a2, (unsigned int)(0xF0000ULL), a4);
    goto loc_00A8F1A3;
}
```

## 5. (Beta) C Style

```c
int64_t PspCreateActivityReference(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint32_t v_stack_m34;
    uint64_t v_stack_m38;
    uint32_t v_stack_m50;
    uint32_t v_stack_m58;
    uint32_t v_stack_m60;
    uint64_t v_stack_m8;
    uint64_t v_stack_p18;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (128);
    Arg1 = 0;
    *(uint64_t *)(local_rsp - 0x48) = v_stack_p18;
    v_stack_m50 = 8;
    v_stack_m38 = 48;
    v_stack_m60 = 8;
    v_stack_m20 = 32;
    v_stack_m18 = v_xmm0;
    result = ObCreateObjectEx(Arg1, *(uint64_t *)(v_rip + 0x538192), v_stack_m38, *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if (!sign_flag) goto loc_00A8F1BD;
loc_00A8F1A3:
    return result;
loc_00A8F1BD:
    Arg2 = 0;
    result = PsChargeProcessWakeCounter(*(uint64_t *)(v_stack_m8 + 0x18), Arg2, Arg2 + 5, v_stack_p18);
    v_stack_m50 = *(uint64_t *)(v_stack_m8 + 0x28);
    a4 = 0;
    Arg2 = 0;
    *(uint64_t *)(v_stack_p18) = result;
    result = ObInsertObjectEx(v_stack_p18, Arg2, (uint32_t)(0xF0000ULL), a4);
    goto loc_00A8F1A3;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A8F110&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A8F110[BB_00A8F110]
  bb_00A8F1A3[BB_00A8F1A3]
  bb_00A8F1BC[BB_00A8F1BC]
  bb_00A8F1BD[BB_00A8F1BD]
  bb_00A8F110 -->|branch| bb_00A8F1BD
  bb_00A8F110 -->|fallthrough| bb_00A8F1A3
  bb_00A8F1BC -->|flow| bb_00A8F1BD
  bb_00A8F1BD -->|branch| bb_00A8F1A3
```
