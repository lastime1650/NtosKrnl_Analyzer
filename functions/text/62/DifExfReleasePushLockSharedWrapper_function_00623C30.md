# DifExfReleasePushLockSharedWrapper

- RVA: `0x00623C30`–`0x00623D80` (길이 `336` bytes)
- VA: `0x0000000140623C30`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D7BC`
- 디코드: `90`개 명령, `336/336` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00623C58` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00623C80` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00623CAE` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00623CD5` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00623CEE` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00623CF6` → [ExfReleasePushLockShared](../26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x00623D1F` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00623D46` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00623D5F` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00623C92` → RVA `0x00F048B8` (`.data`; read)
- `0x00623C9B` → RVA `0x00F04980` (`.data`; read)
- `0x00623CA7` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00623C30  48 8B C4                        mov rax, rsp
00623C33  48 89 58 08                     mov qword ptr [rax + 8], rbx
00623C37  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
00623C3B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00623C3F  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00623C43  41 56                           push r14
00623C45  48 83 EC 30                     sub rsp, 0x30
00623C49  48 8B E9                        mov rbp, rcx
00623C4C  0F 57 C0                        xorps xmm0, xmm0
00623C4F  B9 79 01 00 00                  mov ecx, 0x179
00623C54  0F 11 40 E8                     movups xmmword ptr [rax - 0x18], xmm0
00623C58  E8 D7 1D E7 FF                  call 0x140495a34
00623C5D  48 8B F8                        mov rdi, rax
00623C60  48 85 C0                        test rax, rax
00623C63  0F 84 8A 00 00 00               je 0x140623cf3
00623C69  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00623C6C  A8 18                           test al, 0x18
00623C6E  74 0C                           je 0x140623c7c
00623C70  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
00623C75  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00623C7A  EB 0E                           jmp 0x140623c8a
00623C7C  A8 04                           test al, 4
00623C7E  74 0A                           je 0x140623c8a
00623C80  E8 83 FF EA FF                  call 0x1404d3c08
00623C85  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00623C8A  40 32 F6                        xor sil, sil
00623C8D  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
00623C92  40 38 35 1F 0C 8E 00            cmp byte ptr [rip + 0x8e0c1f], sil
00623C99  75 0C                           jne 0x140623ca7
00623C9B  F7 05 DB 0C 8E 00 00 08 00 00   test dword ptr [rip + 0x8e0cdb], 0x800
00623CA5  74 13                           je 0x140623cba
00623CA7  48 8D 0D D2 01 8E 00            lea rcx, [rip + 0x8e01d2]
00623CAE  E8 6D 29 BF FF                  call 0x140216620
00623CB3  40 8A F0                        mov sil, al
00623CB6  84 C0                           test al, al
00623CB8  74 39                           je 0x140623cf3
00623CBA  4C 8D 77 20                     lea r14, [rdi + 0x20]
00623CBE  49 8B 1E                        mov rbx, qword ptr [r14]
00623CC1  EB 1A                           jmp 0x140623cdd
00623CC3  48 8D 43 F0                     lea rax, [rbx - 0x10]
00623CC7  48 85 C0                        test rax, rax
00623CCA  74 0E                           je 0x140623cda
00623CCC  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00623CD0  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00623CD5  E8 F6 6D 09 00                  call 0x1406baad0
00623CDA  48 8B 1B                        mov rbx, qword ptr [rbx]
00623CDD  49 3B DE                        cmp rbx, r14
00623CE0  75 E1                           jne 0x140623cc3
00623CE2  40 84 F6                        test sil, sil
00623CE5  74 0C                           je 0x140623cf3
00623CE7  48 8D 0D 92 01 8E 00            lea rcx, [rip + 0x8e0192]
00623CEE  E8 8D 61 D2 FF                  call 0x140349e80
00623CF3  48 8B CD                        mov rcx, rbp
00623CF6  E8 45 F7 C3 FF                  call 0x140263440
00623CFB  48 85 FF                        test rdi, rdi
00623CFE  74 64                           je 0x140623d64
00623D00  40 32 F6                        xor sil, sil
00623D03  40 38 35 AE 0B 8E 00            cmp byte ptr [rip + 0x8e0bae], sil
00623D0A  75 0C                           jne 0x140623d18
00623D0C  F7 05 6A 0C 8E 00 00 08 00 00   test dword ptr [rip + 0x8e0c6a], 0x800
00623D16  74 13                           je 0x140623d2b
00623D18  48 8D 0D 61 01 8E 00            lea rcx, [rip + 0x8e0161]
00623D1F  E8 FC 28 BF FF                  call 0x140216620
00623D24  40 8A F0                        mov sil, al
00623D27  84 C0                           test al, al
00623D29  74 39                           je 0x140623d64
00623D2B  48 83 C7 30                     add rdi, 0x30
00623D2F  48 8B 1F                        mov rbx, qword ptr [rdi]
00623D32  EB 1A                           jmp 0x140623d4e
00623D34  48 8D 43 F0                     lea rax, [rbx - 0x10]
00623D38  48 85 C0                        test rax, rax
00623D3B  74 0E                           je 0x140623d4b
00623D3D  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00623D41  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00623D46  E8 85 6D 09 00                  call 0x1406baad0
00623D4B  48 8B 1B                        mov rbx, qword ptr [rbx]
00623D4E  48 3B DF                        cmp rbx, rdi
00623D51  75 E1                           jne 0x140623d34
00623D53  40 84 F6                        test sil, sil
00623D56  74 0C                           je 0x140623d64
00623D58  48 8D 0D 21 01 8E 00            lea rcx, [rip + 0x8e0121]
00623D5F  E8 1C 61 D2 FF                  call 0x140349e80
00623D64  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00623D69  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
00623D6E  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
00623D73  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
00623D78  48 83 C4 30                     add rsp, 0x30
00623D7C  41 5E                           pop r14
00623D7E  C3                              ret
00623D7F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifExfReleasePushLockSharedWrapper(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (48);
    *(unsigned __int64 *)(v_rsp - 24) = v_xmm0;
    result = DifGetAPIThunkContextById(377, a2, a3, a4);
    if (result == 0) goto loc_00623CF3;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00623C7C;
    v_stack_m18 = v_stack_p0;
    goto loc_00623C8A;
loc_00623C7C:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m18 = result;
    }
    v_rsi = 0;
    v_stack_m10 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9309215)) != 0) goto loc_00623CA7;
    if (((*(unsigned int *)(v_rip + 9309403)) & (0x800ULL)) == 0) goto loc_00623CBA;
loc_00623CA7:
    result = ExAcquireRundownProtection(v_rip + 9306578, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00623CF3;
loc_00623CBA:
    goto loc_00623CDD;
loc_00623CC3:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m18;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00623CDD:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00623CC3;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9306514;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ExfReleasePushLockShared(a1, a2, a3, a4);
    if (result == 0) goto loc_00623D64;
    v_rsi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9309102)) != 0) goto loc_00623D18;
    if (((*(unsigned int *)(v_rip + 9309290)) & (0x800ULL)) == 0) goto loc_00623D2B;
loc_00623D18:
    result = ExAcquireRundownProtection(v_rip + 9306465, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00623D64;
loc_00623D2B:
    v_rdi = (result) + (48);
    goto loc_00623D4E;
loc_00623D34:
    result = *(unsigned __int64 *)(v_rdi) - 16;
    if (*(unsigned __int64 *)(v_rdi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi) - 16 + 8);
        a1 = v_stack_m18;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00623D4E:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi))) != v_rdi) goto loc_00623D34;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9306401;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DifExfReleasePushLockSharedWrapper(int64_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (48);
    *(uint64_t *)(local_rsp - 0x18) = v_xmm0;
    result = DifGetAPIThunkContextById(377, a2, a3, a4);
    if (result == 0) goto loc_00623CF3;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00623C7C;
    v_stack_m18 = v_stack_p0;
    goto loc_00623C8A;
loc_00623C7C:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m18 = result;
    }
    local_rsi = 0;
    v_stack_m10 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8E0C1F)) != 0) goto loc_00623CA7;
    if (((*(uint32_t *)(v_rip + 0x8E0CDB)) & (0x800ULL)) == 0) goto loc_00623CBA;
loc_00623CA7:
    result = ExAcquireRundownProtection(v_rip + 9306578, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00623CF3;
loc_00623CBA:
    goto loc_00623CDD;
loc_00623CC3:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m18;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_00623CDD:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00623CC3;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9306514;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = ExfReleasePushLockShared(Arg1, a2, a3, a4);
    if (result == 0) goto loc_00623D64;
    local_rsi = 0;
    if ((*(uint8_t *)(v_rip + 0x8E0BAE)) != 0) goto loc_00623D18;
    if (((*(uint32_t *)(v_rip + 0x8E0C6A)) & (0x800ULL)) == 0) goto loc_00623D2B;
loc_00623D18:
    result = ExAcquireRundownProtection(v_rip + 9306465, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00623D64;
loc_00623D2B:
    local_rdi = (result) + (48);
    goto loc_00623D4E;
loc_00623D34:
    result = *(uint64_t *)(local_rdi) - 16;
    if (*(uint64_t *)(local_rdi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rdi) - 0x10 + 0x8);
        Arg1 = v_stack_m18;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_00623D4E:
    if ((*(uint64_t *)(*(uint64_t *)(local_rdi))) != local_rdi) goto loc_00623D34;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9306401;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (48);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00623C30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00623C30[BB_00623C30]
  bb_00623C69[BB_00623C69]
  bb_00623C70[BB_00623C70]
  bb_00623C7C[BB_00623C7C]
  bb_00623C80[BB_00623C80]
  bb_00623C8A[BB_00623C8A]
  bb_00623C9B[BB_00623C9B]
  bb_00623CA7[BB_00623CA7]
  bb_00623CBA[BB_00623CBA]
  bb_00623CC3[BB_00623CC3]
  bb_00623CCC[BB_00623CCC]
  bb_00623CDA[BB_00623CDA]
  bb_00623CDD[BB_00623CDD]
  bb_00623CE2[BB_00623CE2]
  bb_00623CE7[BB_00623CE7]
  bb_00623CF3[BB_00623CF3]
  bb_00623D00[BB_00623D00]
  bb_00623D0C[BB_00623D0C]
  bb_00623D18[BB_00623D18]
  bb_00623D2B[BB_00623D2B]
  bb_00623D34[BB_00623D34]
  bb_00623D3D[BB_00623D3D]
  bb_00623D4B[BB_00623D4B]
  bb_00623D4E[BB_00623D4E]
  bb_00623D53[BB_00623D53]
  bb_00623D58[BB_00623D58]
  bb_00623D64[BB_00623D64]
  bb_00623D7F[BB_00623D7F]
  bb_00623C30 -->|branch| bb_00623CF3
  bb_00623C30 -->|fallthrough| bb_00623C69
  bb_00623C69 -->|branch| bb_00623C7C
  bb_00623C69 -->|fallthrough| bb_00623C70
  bb_00623C70 -->|branch| bb_00623C8A
  bb_00623C7C -->|branch| bb_00623C8A
  bb_00623C7C -->|fallthrough| bb_00623C80
  bb_00623C80 -->|flow| bb_00623C8A
  bb_00623C8A -->|branch| bb_00623CA7
  bb_00623C8A -->|fallthrough| bb_00623C9B
  bb_00623C9B -->|branch| bb_00623CBA
  bb_00623C9B -->|fallthrough| bb_00623CA7
  bb_00623CA7 -->|branch| bb_00623CF3
  bb_00623CA7 -->|fallthrough| bb_00623CBA
  bb_00623CBA -->|branch| bb_00623CDD
  bb_00623CC3 -->|branch| bb_00623CDA
  bb_00623CC3 -->|fallthrough| bb_00623CCC
  bb_00623CCC -->|flow| bb_00623CDA
  bb_00623CDA -->|flow| bb_00623CDD
  bb_00623CDD -->|branch| bb_00623CC3
  bb_00623CDD -->|fallthrough| bb_00623CE2
  bb_00623CE2 -->|branch| bb_00623CF3
  bb_00623CE2 -->|fallthrough| bb_00623CE7
  bb_00623CE7 -->|flow| bb_00623CF3
  bb_00623CF3 -->|branch| bb_00623D64
  bb_00623CF3 -->|fallthrough| bb_00623D00
  bb_00623D00 -->|branch| bb_00623D18
  bb_00623D00 -->|fallthrough| bb_00623D0C
  bb_00623D0C -->|branch| bb_00623D2B
  bb_00623D0C -->|fallthrough| bb_00623D18
  bb_00623D18 -->|branch| bb_00623D64
  bb_00623D18 -->|fallthrough| bb_00623D2B
  bb_00623D2B -->|branch| bb_00623D4E
  bb_00623D34 -->|branch| bb_00623D4B
  bb_00623D34 -->|fallthrough| bb_00623D3D
  bb_00623D3D -->|flow| bb_00623D4B
  bb_00623D4B -->|flow| bb_00623D4E
  bb_00623D4E -->|branch| bb_00623D34
  bb_00623D4E -->|fallthrough| bb_00623D53
  bb_00623D53 -->|branch| bb_00623D64
  bb_00623D53 -->|fallthrough| bb_00623D58
  bb_00623D58 -->|flow| bb_00623D64
```
