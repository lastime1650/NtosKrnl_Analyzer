# DifZwQueryInformationFileWrapper

- RVA: `0x00646FF0`–`0x00647182` (길이 `402` bytes)
- VA: `0x0000000140646FF0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D2BBC`
- 디코드: `116`개 명령, `402/402` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00647030` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00647056` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00647098` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006470BE` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006470D7` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x006470F0` → [ZwQueryInformationFile](../6A/ZwQueryInformationFile_function_006AD2F0.md) (function, `0x006AD2F0`)
- `0x0064711C` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00647142` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0064715B` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00647066` → RVA `0x00F048B8` (`.data`; read)
- `0x00647085` → RVA `0x00F04980` (`.data`; read)
- `0x00647091` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00646FF0  48 8B C4                        mov rax, rsp
00646FF3  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00646FF7  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00646FFB  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00646FFF  48 89 48 08                     mov qword ptr [rax + 8], rcx
00647003  55                              push rbp
00647004  41 54                           push r12
00647006  41 55                           push r13
00647008  41 56                           push r14
0064700A  41 57                           push r15
0064700C  48 8B EC                        mov rbp, rsp
0064700F  48 83 EC 60                     sub rsp, 0x60
00647013  0F 57 C0                        xorps xmm0, xmm0
00647016  B9 32 00 00 00                  mov ecx, 0x32
0064701B  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0064701F  45 8B F9                        mov r15d, r9d
00647022  4D 8B E0                        mov r12, r8
00647025  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00647029  4C 8B EA                        mov r13, rdx
0064702C  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
00647030  E8 FF E9 E4 FF                  call 0x140495a34
00647035  48 8B F0                        mov rsi, rax
00647038  48 85 C0                        test rax, rax
0064703B  0F 84 9B 00 00 00               je 0x1406470dc
00647041  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00647044  A8 18                           test al, 0x18
00647046  74 0A                           je 0x140647052
00647048  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0064704C  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
00647050  EB 0D                           jmp 0x14064705f
00647052  A8 04                           test al, 4
00647054  74 09                           je 0x14064705f
00647056  E8 AD CB E8 FF                  call 0x1404d3c08
0064705B  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0064705F  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
00647063  45 32 F6                        xor r14b, r14b
00647066  44 38 35 4B D8 8B 00            cmp byte ptr [rip + 0x8bd84b], r14b
0064706D  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00647071  8B 45 50                        mov eax, dword ptr [rbp + 0x50]
00647074  89 45 D8                        mov dword ptr [rbp - 0x28], eax
00647077  4C 89 6D E8                     mov qword ptr [rbp - 0x18], r13
0064707B  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
0064707F  44 89 7D DC                     mov dword ptr [rbp - 0x24], r15d
00647083  75 0C                           jne 0x140647091
00647085  F7 05 F1 D8 8B 00 00 08 00 00   test dword ptr [rip + 0x8bd8f1], 0x800
0064708F  74 13                           je 0x1406470a4
00647091  48 8D 0D E8 CD 8B 00            lea rcx, [rip + 0x8bcde8]
00647098  E8 83 F5 BC FF                  call 0x140216620
0064709D  44 8A F0                        mov r14b, al
006470A0  84 C0                           test al, al
006470A2  74 38                           je 0x1406470dc
006470A4  48 8D 7E 20                     lea rdi, [rsi + 0x20]
006470A8  48 8B 1F                        mov rbx, qword ptr [rdi]
006470AB  EB 19                           jmp 0x1406470c6
006470AD  48 8D 43 F0                     lea rax, [rbx - 0x10]
006470B1  48 85 C0                        test rax, rax
006470B4  74 0D                           je 0x1406470c3
006470B6  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006470BA  48 8D 4D D0                     lea rcx, [rbp - 0x30]
006470BE  E8 0D 3A 07 00                  call 0x1406baad0
006470C3  48 8B 1B                        mov rbx, qword ptr [rbx]
006470C6  48 3B DF                        cmp rbx, rdi
006470C9  75 E2                           jne 0x1406470ad
006470CB  45 84 F6                        test r14b, r14b
006470CE  74 0C                           je 0x1406470dc
006470D0  48 8D 0D A9 CD 8B 00            lea rcx, [rip + 0x8bcda9]
006470D7  E8 A4 2D D0 FF                  call 0x140349e80
006470DC  8B 45 50                        mov eax, dword ptr [rbp + 0x50]
006470DF  45 8B CF                        mov r9d, r15d
006470E2  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
006470E6  4D 8B C4                        mov r8, r12
006470E9  49 8B D5                        mov rdx, r13
006470EC  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
006470F0  E8 FB 61 06 00                  call 0x1406ad2f0
006470F5  89 45 F8                        mov dword ptr [rbp - 8], eax
006470F8  48 85 F6                        test rsi, rsi
006470FB  74 63                           je 0x140647160
006470FD  40 32 FF                        xor dil, dil
00647100  40 38 3D B1 D7 8B 00            cmp byte ptr [rip + 0x8bd7b1], dil
00647107  75 0C                           jne 0x140647115
00647109  F7 05 6D D8 8B 00 00 08 00 00   test dword ptr [rip + 0x8bd86d], 0x800
00647113  74 13                           je 0x140647128
00647115  48 8D 0D 64 CD 8B 00            lea rcx, [rip + 0x8bcd64]
0064711C  E8 FF F4 BC FF                  call 0x140216620
00647121  40 8A F8                        mov dil, al
00647124  84 C0                           test al, al
00647126  74 38                           je 0x140647160
00647128  48 83 C6 30                     add rsi, 0x30
0064712C  48 8B 1E                        mov rbx, qword ptr [rsi]
0064712F  EB 19                           jmp 0x14064714a
00647131  48 8D 43 F0                     lea rax, [rbx - 0x10]
00647135  48 85 C0                        test rax, rax
00647138  74 0D                           je 0x140647147
0064713A  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0064713E  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00647142  E8 89 39 07 00                  call 0x1406baad0
00647147  48 8B 1B                        mov rbx, qword ptr [rbx]
0064714A  48 3B DE                        cmp rbx, rsi
0064714D  75 E2                           jne 0x140647131
0064714F  40 84 FF                        test dil, dil
00647152  74 0C                           je 0x140647160
00647154  48 8D 0D 25 CD 8B 00            lea rcx, [rip + 0x8bcd25]
0064715B  E8 20 2D D0 FF                  call 0x140349e80
00647160  8B 45 F8                        mov eax, dword ptr [rbp - 8]
00647163  4C 8D 5C 24 60                  lea r11, [rsp + 0x60]
00647168  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0064716C  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00647170  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00647174  49 8B E3                        mov rsp, r11
00647177  41 5F                           pop r15
00647179  41 5E                           pop r14
0064717B  41 5D                           pop r13
0064717D  41 5C                           pop r12
0064717F  5D                              pop rbp
00647180  C3                              ret
00647181  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwQueryInformationFileWrapper(__int64 a1, __int64 a2, __int64 a3, int a4, unsigned int a5)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m4C;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (96);
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = DifGetAPIThunkContextById(50, a2, a3, a4);
    if (result == 0) goto loc_006470DC;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00647052;
    v_stack_m58 = v_stack_p0;
    goto loc_0064705F;
loc_00647052:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m50 = (unsigned int)((unsigned int)(a5));
    v_stack_m40 = a2;
    v_stack_m48 = a3;
    v_stack_m4C = (unsigned int)((unsigned int)(a4));
    if ((*(unsigned __int8 *)(v_rip + 9164875)) != 0) goto loc_00647091;
    if (((*(unsigned int *)(v_rip + 9165041)) & (0x800ULL)) == 0) goto loc_006470A4;
loc_00647091:
    result = ExAcquireRundownProtection(v_rip + 9162216, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006470DC;
loc_006470A4:
    goto loc_006470C6;
loc_006470AD:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006470C6:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_006470AD;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9162153;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_stack_m68 = (unsigned int)((unsigned int)(a5));
    result = ZwQueryInformationFile(v_stack_p8, a2, a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    v_stack_m30 = (unsigned int)(result);
    if (result == 0) goto loc_00647160;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9164721)) != 0) goto loc_00647115;
    if (((*(unsigned int *)(v_rip + 9164909)) & (0x800ULL)) == 0) goto loc_00647128;
loc_00647115:
    result = ExAcquireRundownProtection(v_rip + 9162084, a2, a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    if ((unsigned __int8)(result) == 0) goto loc_00647160;
loc_00647128:
    v_rsi = (result) + (48);
    goto loc_0064714A;
loc_00647131:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
loc_0064714A:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00647131;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9162021;
        result = ExReleaseRundownProtection(a1, a2, a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
    return (unsigned int)(v_stack_m30);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwQueryInformationFileWrapper(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, uint32_t Arg5)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_m4C;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m68;
    uint64_t v_stack_p0;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (96);
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = DifGetAPIThunkContextById(50, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_006470DC;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00647052;
    v_stack_m58 = v_stack_p0;
    goto loc_0064705F;
loc_00647052:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m50 = (uint32_t)((uint32_t)(Arg5));
    v_stack_m40 = Arg2;
    v_stack_m48 = Arg3;
    v_stack_m4C = (uint32_t)((uint32_t)(Arg4));
    if ((*(uint8_t *)(v_rip + 0x8BD84B)) != 0) goto loc_00647091;
    if (((*(uint32_t *)(v_rip + 0x8BD8F1)) & (0x800ULL)) == 0) goto loc_006470A4;
loc_00647091:
    result = ExAcquireRundownProtection(v_rip + 9162216, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_006470DC;
loc_006470A4:
    goto loc_006470C6;
loc_006470AD:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_006470C6:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_006470AD;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9162153;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m68 = (uint32_t)((uint32_t)(Arg5));
    result = ZwQueryInformationFile(v_stack_p8, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    v_stack_m30 = (uint32_t)(result);
    if (result == 0) goto loc_00647160;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8BD7B1)) != 0) goto loc_00647115;
    if (((*(uint32_t *)(v_rip + 0x8BD86D)) & (0x800ULL)) == 0) goto loc_00647128;
loc_00647115:
    result = ExAcquireRundownProtection(v_rip + 9162084, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    if ((uint8_t)(result) == 0) goto loc_00647160;
loc_00647128:
    local_rsi = (result) + (48);
    goto loc_0064714A;
loc_00647131:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
loc_0064714A:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00647131;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9162021;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
    return (uint32_t)(v_stack_m30);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00646FF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00646FF0[BB_00646FF0]
  bb_00647041[BB_00647041]
  bb_00647048[BB_00647048]
  bb_00647052[BB_00647052]
  bb_00647056[BB_00647056]
  bb_0064705F[BB_0064705F]
  bb_00647085[BB_00647085]
  bb_00647091[BB_00647091]
  bb_006470A4[BB_006470A4]
  bb_006470AD[BB_006470AD]
  bb_006470B6[BB_006470B6]
  bb_006470C3[BB_006470C3]
  bb_006470C6[BB_006470C6]
  bb_006470CB[BB_006470CB]
  bb_006470D0[BB_006470D0]
  bb_006470DC[BB_006470DC]
  bb_006470FD[BB_006470FD]
  bb_00647109[BB_00647109]
  bb_00647115[BB_00647115]
  bb_00647128[BB_00647128]
  bb_00647131[BB_00647131]
  bb_0064713A[BB_0064713A]
  bb_00647147[BB_00647147]
  bb_0064714A[BB_0064714A]
  bb_0064714F[BB_0064714F]
  bb_00647154[BB_00647154]
  bb_00647160[BB_00647160]
  bb_00647181[BB_00647181]
  bb_00646FF0 -->|branch| bb_006470DC
  bb_00646FF0 -->|fallthrough| bb_00647041
  bb_00647041 -->|branch| bb_00647052
  bb_00647041 -->|fallthrough| bb_00647048
  bb_00647048 -->|branch| bb_0064705F
  bb_00647052 -->|branch| bb_0064705F
  bb_00647052 -->|fallthrough| bb_00647056
  bb_00647056 -->|flow| bb_0064705F
  bb_0064705F -->|branch| bb_00647091
  bb_0064705F -->|fallthrough| bb_00647085
  bb_00647085 -->|branch| bb_006470A4
  bb_00647085 -->|fallthrough| bb_00647091
  bb_00647091 -->|branch| bb_006470DC
  bb_00647091 -->|fallthrough| bb_006470A4
  bb_006470A4 -->|branch| bb_006470C6
  bb_006470AD -->|branch| bb_006470C3
  bb_006470AD -->|fallthrough| bb_006470B6
  bb_006470B6 -->|flow| bb_006470C3
  bb_006470C3 -->|flow| bb_006470C6
  bb_006470C6 -->|branch| bb_006470AD
  bb_006470C6 -->|fallthrough| bb_006470CB
  bb_006470CB -->|branch| bb_006470DC
  bb_006470CB -->|fallthrough| bb_006470D0
  bb_006470D0 -->|flow| bb_006470DC
  bb_006470DC -->|branch| bb_00647160
  bb_006470DC -->|fallthrough| bb_006470FD
  bb_006470FD -->|branch| bb_00647115
  bb_006470FD -->|fallthrough| bb_00647109
  bb_00647109 -->|branch| bb_00647128
  bb_00647109 -->|fallthrough| bb_00647115
  bb_00647115 -->|branch| bb_00647160
  bb_00647115 -->|fallthrough| bb_00647128
  bb_00647128 -->|branch| bb_0064714A
  bb_00647131 -->|branch| bb_00647147
  bb_00647131 -->|fallthrough| bb_0064713A
  bb_0064713A -->|flow| bb_00647147
  bb_00647147 -->|flow| bb_0064714A
  bb_0064714A -->|branch| bb_00647131
  bb_0064714A -->|fallthrough| bb_0064714F
  bb_0064714F -->|branch| bb_00647160
  bb_0064714F -->|fallthrough| bb_00647154
  bb_00647154 -->|flow| bb_00647160
```
