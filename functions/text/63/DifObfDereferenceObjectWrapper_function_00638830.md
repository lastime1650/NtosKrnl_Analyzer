# DifObfDereferenceObjectWrapper

- RVA: `0x00638830`–`0x00638996` (길이 `358` bytes)
- VA: `0x0000000140638830`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060130`
- 디코드: `95`개 명령, `358/358` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0063885F` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00638887` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x006388B5` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006388DC` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006388F5` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00638902` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00638930` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00638957` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00638970` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00638899` → RVA `0x00F048B8` (`.data`; read)
- `0x006388A2` → RVA `0x00F04980` (`.data`; read)
- `0x006388AE` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00638830  4C 8B DC                        mov r11, rsp
00638833  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00638837  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
0063883B  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
0063883F  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
00638843  41 56                           push r14
00638845  48 83 EC 40                     sub rsp, 0x40
00638849  33 C0                           xor eax, eax
0063884B  0F 57 C0                        xorps xmm0, xmm0
0063884E  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
00638853  48 8B E9                        mov rbp, rcx
00638856  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
0063885A  B9 C6 00 00 00                  mov ecx, 0xc6
0063885F  E8 D0 D1 E5 FF                  call 0x140495a34
00638864  48 8B F0                        mov rsi, rax
00638867  48 85 C0                        test rax, rax
0063886A  0F 84 8A 00 00 00               je 0x1406388fa
00638870  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00638873  A8 18                           test al, 0x18
00638875  74 0C                           je 0x140638883
00638877  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0063887C  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00638881  EB 0E                           jmp 0x140638891
00638883  A8 04                           test al, 4
00638885  74 0A                           je 0x140638891
00638887  E8 7C B3 E9 FF                  call 0x1404d3c08
0063888C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00638891  40 32 FF                        xor dil, dil
00638894  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
00638899  40 38 3D 18 C0 8C 00            cmp byte ptr [rip + 0x8cc018], dil
006388A0  75 0C                           jne 0x1406388ae
006388A2  F7 05 D4 C0 8C 00 00 08 00 00   test dword ptr [rip + 0x8cc0d4], 0x800
006388AC  74 13                           je 0x1406388c1
006388AE  48 8D 0D CB B5 8C 00            lea rcx, [rip + 0x8cb5cb]
006388B5  E8 66 DD BD FF                  call 0x140216620
006388BA  40 8A F8                        mov dil, al
006388BD  84 C0                           test al, al
006388BF  74 39                           je 0x1406388fa
006388C1  4C 8D 76 20                     lea r14, [rsi + 0x20]
006388C5  49 8B 1E                        mov rbx, qword ptr [r14]
006388C8  EB 1A                           jmp 0x1406388e4
006388CA  48 8D 43 F0                     lea rax, [rbx - 0x10]
006388CE  48 85 C0                        test rax, rax
006388D1  74 0E                           je 0x1406388e1
006388D3  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006388D7  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
006388DC  E8 EF 21 08 00                  call 0x1406baad0
006388E1  48 8B 1B                        mov rbx, qword ptr [rbx]
006388E4  49 3B DE                        cmp rbx, r14
006388E7  75 E1                           jne 0x1406388ca
006388E9  40 84 FF                        test dil, dil
006388EC  74 0C                           je 0x1406388fa
006388EE  48 8D 0D 8B B5 8C 00            lea rcx, [rip + 0x8cb58b]
006388F5  E8 86 15 D1 FF                  call 0x140349e80
006388FA  BA 44 66 6C 74                  mov edx, 0x746c6644
006388FF  48 8B CD                        mov rcx, rbp
00638902  E8 D9 EF CB FF                  call 0x1402f78e0
00638907  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0063890C  48 85 F6                        test rsi, rsi
0063890F  74 64                           je 0x140638975
00638911  40 32 FF                        xor dil, dil
00638914  40 38 3D 9D BF 8C 00            cmp byte ptr [rip + 0x8cbf9d], dil
0063891B  75 0C                           jne 0x140638929
0063891D  F7 05 59 C0 8C 00 00 08 00 00   test dword ptr [rip + 0x8cc059], 0x800
00638927  74 13                           je 0x14063893c
00638929  48 8D 0D 50 B5 8C 00            lea rcx, [rip + 0x8cb550]
00638930  E8 EB DC BD FF                  call 0x140216620
00638935  40 8A F8                        mov dil, al
00638938  84 C0                           test al, al
0063893A  74 39                           je 0x140638975
0063893C  48 83 C6 30                     add rsi, 0x30
00638940  48 8B 1E                        mov rbx, qword ptr [rsi]
00638943  EB 1A                           jmp 0x14063895f
00638945  48 8D 43 F0                     lea rax, [rbx - 0x10]
00638949  48 85 C0                        test rax, rax
0063894C  74 0E                           je 0x14063895c
0063894E  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00638952  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00638957  E8 74 21 08 00                  call 0x1406baad0
0063895C  48 8B 1B                        mov rbx, qword ptr [rbx]
0063895F  48 3B DE                        cmp rbx, rsi
00638962  75 E1                           jne 0x140638945
00638964  40 84 FF                        test dil, dil
00638967  74 0C                           je 0x140638975
00638969  48 8D 0D 10 B5 8C 00            lea rcx, [rip + 0x8cb510]
00638970  E8 0B 15 D1 FF                  call 0x140349e80
00638975  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
0063897A  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
0063897F  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
00638984  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
00638989  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
0063898E  48 83 C4 40                     add rsp, 0x40
00638992  41 5E                           pop r14
00638994  C3                              ret
00638995  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifObfDereferenceObjectWrapper(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (64);
    result = 0;
    v_stack_m28 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 24) = 0;
    result = DifGetAPIThunkContextById(198, a2, a3, a4);
    if (result == 0) goto loc_006388FA;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00638883;
    v_stack_m28 = v_stack_p0;
    goto loc_00638891;
loc_00638883:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_rdi = 0;
    v_stack_m20 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9224216)) != 0) goto loc_006388AE;
    if (((*(unsigned int *)(v_rip + 9224404)) & (0x800ULL)) == 0) goto loc_006388C1;
loc_006388AE:
    result = ExAcquireRundownProtection(v_rip + 9221579, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006388FA;
loc_006388C1:
    goto loc_006388E4;
loc_006388CA:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006388E4:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_006388CA;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9221515;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ObfDereferenceObjectWithTag(a1, (unsigned int)(0x746C6644ULL), a3, a4);
    v_stack_m18 = result;
    if (result == 0) goto loc_00638975;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9224093)) != 0) goto loc_00638929;
    if (((*(unsigned int *)(v_rip + 9224281)) & (0x800ULL)) == 0) goto loc_0063893C;
loc_00638929:
    result = ExAcquireRundownProtection(v_rip + 9221456, (unsigned int)(0x746C6644ULL), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00638975;
loc_0063893C:
    v_rsi = (result) + (48);
    goto loc_0063895F;
loc_00638945:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, (unsigned int)(0x746C6644ULL), a3, a4);
    }
loc_0063895F:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00638945;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9221392;
        result = ExReleaseRundownProtection(a1, (unsigned int)(0x746C6644ULL), a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return v_stack_m18;
}
```

## 5. (Beta) C Style

```c
int64_t DifObfDereferenceObjectWrapper(int64_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (64);
    result = 0;
    v_stack_m28 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x18) = 0;
    result = DifGetAPIThunkContextById(198, a2, a3, a4);
    if (result == 0) goto loc_006388FA;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00638883;
    v_stack_m28 = v_stack_p0;
    goto loc_00638891;
loc_00638883:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    local_rdi = 0;
    v_stack_m20 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8CC018)) != 0) goto loc_006388AE;
    if (((*(uint32_t *)(v_rip + 0x8CC0D4)) & (0x800ULL)) == 0) goto loc_006388C1;
loc_006388AE:
    result = ExAcquireRundownProtection(v_rip + 9221579, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_006388FA;
loc_006388C1:
    goto loc_006388E4;
loc_006388CA:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_006388E4:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_006388CA;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9221515;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = ObfDereferenceObjectWithTag(Arg1, (uint32_t)(0x746C6644ULL), a3, a4);
    v_stack_m18 = result;
    if (result == 0) goto loc_00638975;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8CBF9D)) != 0) goto loc_00638929;
    if (((*(uint32_t *)(v_rip + 0x8CC059)) & (0x800ULL)) == 0) goto loc_0063893C;
loc_00638929:
    result = ExAcquireRundownProtection(v_rip + 9221456, (uint32_t)(0x746C6644ULL), a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00638975;
loc_0063893C:
    local_rsi = (result) + (48);
    goto loc_0063895F;
loc_00638945:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, (uint32_t)(0x746C6644ULL), a3, a4);
    }
loc_0063895F:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00638945;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9221392;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)(0x746C6644ULL), a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return v_stack_m18;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00638830&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00638830[BB_00638830]
  bb_00638870[BB_00638870]
  bb_00638877[BB_00638877]
  bb_00638883[BB_00638883]
  bb_00638887[BB_00638887]
  bb_00638891[BB_00638891]
  bb_006388A2[BB_006388A2]
  bb_006388AE[BB_006388AE]
  bb_006388C1[BB_006388C1]
  bb_006388CA[BB_006388CA]
  bb_006388D3[BB_006388D3]
  bb_006388E1[BB_006388E1]
  bb_006388E4[BB_006388E4]
  bb_006388E9[BB_006388E9]
  bb_006388EE[BB_006388EE]
  bb_006388FA[BB_006388FA]
  bb_00638911[BB_00638911]
  bb_0063891D[BB_0063891D]
  bb_00638929[BB_00638929]
  bb_0063893C[BB_0063893C]
  bb_00638945[BB_00638945]
  bb_0063894E[BB_0063894E]
  bb_0063895C[BB_0063895C]
  bb_0063895F[BB_0063895F]
  bb_00638964[BB_00638964]
  bb_00638969[BB_00638969]
  bb_00638975[BB_00638975]
  bb_00638995[BB_00638995]
  bb_00638830 -->|branch| bb_006388FA
  bb_00638830 -->|fallthrough| bb_00638870
  bb_00638870 -->|branch| bb_00638883
  bb_00638870 -->|fallthrough| bb_00638877
  bb_00638877 -->|branch| bb_00638891
  bb_00638883 -->|branch| bb_00638891
  bb_00638883 -->|fallthrough| bb_00638887
  bb_00638887 -->|flow| bb_00638891
  bb_00638891 -->|branch| bb_006388AE
  bb_00638891 -->|fallthrough| bb_006388A2
  bb_006388A2 -->|branch| bb_006388C1
  bb_006388A2 -->|fallthrough| bb_006388AE
  bb_006388AE -->|branch| bb_006388FA
  bb_006388AE -->|fallthrough| bb_006388C1
  bb_006388C1 -->|branch| bb_006388E4
  bb_006388CA -->|branch| bb_006388E1
  bb_006388CA -->|fallthrough| bb_006388D3
  bb_006388D3 -->|flow| bb_006388E1
  bb_006388E1 -->|flow| bb_006388E4
  bb_006388E4 -->|branch| bb_006388CA
  bb_006388E4 -->|fallthrough| bb_006388E9
  bb_006388E9 -->|branch| bb_006388FA
  bb_006388E9 -->|fallthrough| bb_006388EE
  bb_006388EE -->|flow| bb_006388FA
  bb_006388FA -->|branch| bb_00638975
  bb_006388FA -->|fallthrough| bb_00638911
  bb_00638911 -->|branch| bb_00638929
  bb_00638911 -->|fallthrough| bb_0063891D
  bb_0063891D -->|branch| bb_0063893C
  bb_0063891D -->|fallthrough| bb_00638929
  bb_00638929 -->|branch| bb_00638975
  bb_00638929 -->|fallthrough| bb_0063893C
  bb_0063893C -->|branch| bb_0063895F
  bb_00638945 -->|branch| bb_0063895C
  bb_00638945 -->|fallthrough| bb_0063894E
  bb_0063894E -->|flow| bb_0063895C
  bb_0063895C -->|flow| bb_0063895F
  bb_0063895F -->|branch| bb_00638945
  bb_0063895F -->|fallthrough| bb_00638964
  bb_00638964 -->|branch| bb_00638975
  bb_00638964 -->|fallthrough| bb_00638969
  bb_00638969 -->|flow| bb_00638975
```
