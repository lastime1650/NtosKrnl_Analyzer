# DifKeCancelTimerWrapper

- RVA: `0x0062EE20`–`0x0062EF7F` (길이 `351` bytes)
- VA: `0x000000014062EE20`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060130`
- 디코드: `94`개 명령, `351/351` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0062EE4F` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0062EE77` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0062EEA5` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062EECC` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062EEE5` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0062EEED` → [KeCancelTimer](../23/KeCancelTimer_function_002327E0.md) (function, `0x002327E0`)
- `0x0062EF1A` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062EF41` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062EF5A` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0062EE89` → RVA `0x00F048B8` (`.data`; read)
- `0x0062EE92` → RVA `0x00F04980` (`.data`; read)
- `0x0062EE9E` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0062EE20  4C 8B DC                        mov r11, rsp
0062EE23  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
0062EE27  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
0062EE2B  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
0062EE2F  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
0062EE33  41 56                           push r14
0062EE35  48 83 EC 40                     sub rsp, 0x40
0062EE39  33 C0                           xor eax, eax
0062EE3B  0F 57 C0                        xorps xmm0, xmm0
0062EE3E  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
0062EE43  48 8B E9                        mov rbp, rcx
0062EE46  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
0062EE4A  B9 22 01 00 00                  mov ecx, 0x122
0062EE4F  E8 E0 6B E6 FF                  call 0x140495a34
0062EE54  48 8B F0                        mov rsi, rax
0062EE57  48 85 C0                        test rax, rax
0062EE5A  0F 84 8A 00 00 00               je 0x14062eeea
0062EE60  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0062EE63  A8 18                           test al, 0x18
0062EE65  74 0C                           je 0x14062ee73
0062EE67  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0062EE6C  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0062EE71  EB 0E                           jmp 0x14062ee81
0062EE73  A8 04                           test al, 4
0062EE75  74 0A                           je 0x14062ee81
0062EE77  E8 8C 4D EA FF                  call 0x1404d3c08
0062EE7C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0062EE81  40 32 FF                        xor dil, dil
0062EE84  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
0062EE89  40 38 3D 28 5A 8D 00            cmp byte ptr [rip + 0x8d5a28], dil
0062EE90  75 0C                           jne 0x14062ee9e
0062EE92  F7 05 E4 5A 8D 00 00 08 00 00   test dword ptr [rip + 0x8d5ae4], 0x800
0062EE9C  74 13                           je 0x14062eeb1
0062EE9E  48 8D 0D DB 4F 8D 00            lea rcx, [rip + 0x8d4fdb]
0062EEA5  E8 76 77 BE FF                  call 0x140216620
0062EEAA  40 8A F8                        mov dil, al
0062EEAD  84 C0                           test al, al
0062EEAF  74 39                           je 0x14062eeea
0062EEB1  4C 8D 76 20                     lea r14, [rsi + 0x20]
0062EEB5  49 8B 1E                        mov rbx, qword ptr [r14]
0062EEB8  EB 1A                           jmp 0x14062eed4
0062EEBA  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062EEBE  48 85 C0                        test rax, rax
0062EEC1  74 0E                           je 0x14062eed1
0062EEC3  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062EEC7  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062EECC  E8 FF BB 08 00                  call 0x1406baad0
0062EED1  48 8B 1B                        mov rbx, qword ptr [rbx]
0062EED4  49 3B DE                        cmp rbx, r14
0062EED7  75 E1                           jne 0x14062eeba
0062EED9  40 84 FF                        test dil, dil
0062EEDC  74 0C                           je 0x14062eeea
0062EEDE  48 8D 0D 9B 4F 8D 00            lea rcx, [rip + 0x8d4f9b]
0062EEE5  E8 96 AF D1 FF                  call 0x140349e80
0062EEEA  48 8B CD                        mov rcx, rbp
0062EEED  E8 EE 38 C0 FF                  call 0x1402327e0
0062EEF2  88 44 24 30                     mov byte ptr [rsp + 0x30], al
0062EEF6  48 85 F6                        test rsi, rsi
0062EEF9  74 64                           je 0x14062ef5f
0062EEFB  40 32 FF                        xor dil, dil
0062EEFE  40 38 3D B3 59 8D 00            cmp byte ptr [rip + 0x8d59b3], dil
0062EF05  75 0C                           jne 0x14062ef13
0062EF07  F7 05 6F 5A 8D 00 00 08 00 00   test dword ptr [rip + 0x8d5a6f], 0x800
0062EF11  74 13                           je 0x14062ef26
0062EF13  48 8D 0D 66 4F 8D 00            lea rcx, [rip + 0x8d4f66]
0062EF1A  E8 01 77 BE FF                  call 0x140216620
0062EF1F  40 8A F8                        mov dil, al
0062EF22  84 C0                           test al, al
0062EF24  74 39                           je 0x14062ef5f
0062EF26  48 83 C6 30                     add rsi, 0x30
0062EF2A  48 8B 1E                        mov rbx, qword ptr [rsi]
0062EF2D  EB 1A                           jmp 0x14062ef49
0062EF2F  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062EF33  48 85 C0                        test rax, rax
0062EF36  74 0E                           je 0x14062ef46
0062EF38  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062EF3C  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062EF41  E8 8A BB 08 00                  call 0x1406baad0
0062EF46  48 8B 1B                        mov rbx, qword ptr [rbx]
0062EF49  48 3B DE                        cmp rbx, rsi
0062EF4C  75 E1                           jne 0x14062ef2f
0062EF4E  40 84 FF                        test dil, dil
0062EF51  74 0C                           je 0x14062ef5f
0062EF53  48 8D 0D 26 4F 8D 00            lea rcx, [rip + 0x8d4f26]
0062EF5A  E8 21 AF D1 FF                  call 0x140349e80
0062EF5F  8A 44 24 30                     mov al, byte ptr [rsp + 0x30]
0062EF63  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
0062EF68  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
0062EF6D  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
0062EF72  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
0062EF77  48 83 C4 40                     add rsp, 0x40
0062EF7B  41 5E                           pop r14
0062EF7D  C3                              ret
0062EF7E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifKeCancelTimerWrapper(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int8 v_stack_m18;
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
    result = DifGetAPIThunkContextById(290, a2, a3, a4);
    if (result == 0) goto loc_0062EEEA;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0062EE73;
    v_stack_m28 = v_stack_p0;
    goto loc_0062EE81;
loc_0062EE73:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_rdi = 0;
    v_stack_m20 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9263656)) != 0) goto loc_0062EE9E;
    if (((*(unsigned int *)(v_rip + 9263844)) & (0x800ULL)) == 0) goto loc_0062EEB1;
loc_0062EE9E:
    result = ExAcquireRundownProtection(v_rip + 9261019, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062EEEA;
loc_0062EEB1:
    goto loc_0062EED4;
loc_0062EEBA:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062EED4:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0062EEBA;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9260955;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = KeCancelTimer(a1, a2, a3, a4);
    v_stack_m18 = (unsigned __int8)(result);
    if (result == 0) goto loc_0062EF5F;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9263539)) != 0) goto loc_0062EF13;
    if (((*(unsigned int *)(v_rip + 9263727)) & (0x800ULL)) == 0) goto loc_0062EF26;
loc_0062EF13:
    result = ExAcquireRundownProtection(v_rip + 9260902, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062EF5F;
loc_0062EF26:
    v_rsi = (result) + (48);
    goto loc_0062EF49;
loc_0062EF2F:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062EF49:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0062EF2F;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9260838;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return v_stack_m18;
}
```

## 5. (Beta) C Style

```c
int64_t DifKeCancelTimerWrapper(int64_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint8_t v_stack_m18;
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
    result = DifGetAPIThunkContextById(290, a2, a3, a4);
    if (result == 0) goto loc_0062EEEA;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0062EE73;
    v_stack_m28 = v_stack_p0;
    goto loc_0062EE81;
loc_0062EE73:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    local_rdi = 0;
    v_stack_m20 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8D5A28)) != 0) goto loc_0062EE9E;
    if (((*(uint32_t *)(v_rip + 0x8D5AE4)) & (0x800ULL)) == 0) goto loc_0062EEB1;
loc_0062EE9E:
    result = ExAcquireRundownProtection(v_rip + 9261019, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062EEEA;
loc_0062EEB1:
    goto loc_0062EED4;
loc_0062EEBA:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0062EED4:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0062EEBA;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9260955;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = KeCancelTimer(Arg1, a2, a3, a4);
    v_stack_m18 = (uint8_t)(result);
    if (result == 0) goto loc_0062EF5F;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D59B3)) != 0) goto loc_0062EF13;
    if (((*(uint32_t *)(v_rip + 0x8D5A6F)) & (0x800ULL)) == 0) goto loc_0062EF26;
loc_0062EF13:
    result = ExAcquireRundownProtection(v_rip + 9260902, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062EF5F;
loc_0062EF26:
    local_rsi = (result) + (48);
    goto loc_0062EF49;
loc_0062EF2F:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0062EF49:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0062EF2F;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9260838;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return v_stack_m18;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0062EE20&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0062EE20[BB_0062EE20]
  bb_0062EE60[BB_0062EE60]
  bb_0062EE67[BB_0062EE67]
  bb_0062EE73[BB_0062EE73]
  bb_0062EE77[BB_0062EE77]
  bb_0062EE81[BB_0062EE81]
  bb_0062EE92[BB_0062EE92]
  bb_0062EE9E[BB_0062EE9E]
  bb_0062EEB1[BB_0062EEB1]
  bb_0062EEBA[BB_0062EEBA]
  bb_0062EEC3[BB_0062EEC3]
  bb_0062EED1[BB_0062EED1]
  bb_0062EED4[BB_0062EED4]
  bb_0062EED9[BB_0062EED9]
  bb_0062EEDE[BB_0062EEDE]
  bb_0062EEEA[BB_0062EEEA]
  bb_0062EEFB[BB_0062EEFB]
  bb_0062EF07[BB_0062EF07]
  bb_0062EF13[BB_0062EF13]
  bb_0062EF26[BB_0062EF26]
  bb_0062EF2F[BB_0062EF2F]
  bb_0062EF38[BB_0062EF38]
  bb_0062EF46[BB_0062EF46]
  bb_0062EF49[BB_0062EF49]
  bb_0062EF4E[BB_0062EF4E]
  bb_0062EF53[BB_0062EF53]
  bb_0062EF5F[BB_0062EF5F]
  bb_0062EF7E[BB_0062EF7E]
  bb_0062EE20 -->|branch| bb_0062EEEA
  bb_0062EE20 -->|fallthrough| bb_0062EE60
  bb_0062EE60 -->|branch| bb_0062EE73
  bb_0062EE60 -->|fallthrough| bb_0062EE67
  bb_0062EE67 -->|branch| bb_0062EE81
  bb_0062EE73 -->|branch| bb_0062EE81
  bb_0062EE73 -->|fallthrough| bb_0062EE77
  bb_0062EE77 -->|flow| bb_0062EE81
  bb_0062EE81 -->|branch| bb_0062EE9E
  bb_0062EE81 -->|fallthrough| bb_0062EE92
  bb_0062EE92 -->|branch| bb_0062EEB1
  bb_0062EE92 -->|fallthrough| bb_0062EE9E
  bb_0062EE9E -->|branch| bb_0062EEEA
  bb_0062EE9E -->|fallthrough| bb_0062EEB1
  bb_0062EEB1 -->|branch| bb_0062EED4
  bb_0062EEBA -->|branch| bb_0062EED1
  bb_0062EEBA -->|fallthrough| bb_0062EEC3
  bb_0062EEC3 -->|flow| bb_0062EED1
  bb_0062EED1 -->|flow| bb_0062EED4
  bb_0062EED4 -->|branch| bb_0062EEBA
  bb_0062EED4 -->|fallthrough| bb_0062EED9
  bb_0062EED9 -->|branch| bb_0062EEEA
  bb_0062EED9 -->|fallthrough| bb_0062EEDE
  bb_0062EEDE -->|flow| bb_0062EEEA
  bb_0062EEEA -->|branch| bb_0062EF5F
  bb_0062EEEA -->|fallthrough| bb_0062EEFB
  bb_0062EEFB -->|branch| bb_0062EF13
  bb_0062EEFB -->|fallthrough| bb_0062EF07
  bb_0062EF07 -->|branch| bb_0062EF26
  bb_0062EF07 -->|fallthrough| bb_0062EF13
  bb_0062EF13 -->|branch| bb_0062EF5F
  bb_0062EF13 -->|fallthrough| bb_0062EF26
  bb_0062EF26 -->|branch| bb_0062EF49
  bb_0062EF2F -->|branch| bb_0062EF46
  bb_0062EF2F -->|fallthrough| bb_0062EF38
  bb_0062EF38 -->|flow| bb_0062EF46
  bb_0062EF46 -->|flow| bb_0062EF49
  bb_0062EF49 -->|branch| bb_0062EF2F
  bb_0062EF49 -->|fallthrough| bb_0062EF4E
  bb_0062EF4E -->|branch| bb_0062EF5F
  bb_0062EF4E -->|fallthrough| bb_0062EF53
  bb_0062EF53 -->|flow| bb_0062EF5F
```
