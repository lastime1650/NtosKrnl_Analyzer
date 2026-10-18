# MiWaitForVadDeletion

- RVA: `0x00316F1C`–`0x00316FC3` (길이 `167` bytes)
- VA: `0x0000000140316F1C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000749E8`
- 디코드: `42`개 명령, `167/167` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00316F3E` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00316F82` → [MiInsertVadEvent](../43/MiInsertVadEvent_function_00430E74.md) (function, `0x00430E74`)
- `0x00316F8D` → [MiUnlockVad](../2A/MiUnlockVad_function_002A59C8.md) (function, `0x002A59C8`)
- `0x00316F9D` → [KeWaitForGate](../2C/KeWaitForGate_function_002CA794.md) (function, `0x002CA794`)
- `0x00316FA8` → [MiLockVad](../29/MiLockVad_function_00295810.md) (function, `0x00295810`)

### Direct callers
- [MiObtainReferencedSecureVad](../29/MiObtainReferencedSecureVad_function_00295688.md) at `0x002957E1`
- [MiReturnLockedVadOrNextVa](MiReturnLockedVadOrNextVa_function_00316980.md) at `0x00316CE6`
- [sub_006E13DC](../6E/Unknown_function_006E13DC.md) at `0x006E13DF`
- [MiLockVadRange](../../page/87/MiLockVadRange_function_0087F670.md) at `0x0087F94C`
- [MiCleanVad](../../page/88/MiCleanVad_function_00889224.md) at `0x00889264`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00316F1C  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00316F21  48 89 7C 24 10                  mov qword ptr [rsp + 0x10], rdi
00316F26  55                              push rbp
00316F27  48 8B EC                        mov rbp, rsp
00316F2A  48 81 EC 80 00 00 00            sub rsp, 0x80
00316F31  33 D2                           xor edx, edx
00316F33  48 8B F9                        mov rdi, rcx
00316F36  48 8D 4D A0                     lea rcx, [rbp - 0x60]
00316F3A  44 8D 42 58                     lea r8d, [rdx + 0x58]
00316F3E  E8 FD FC 3A 00                  call 0x1406c6c40
00316F43  48 83 7F 10 FF                  cmp qword ptr [rdi + 0x10], -1
00316F48  74 63                           je 0x140316fad
00316F4A  65 48 8B 1C 25 88 01 00 00      mov rbx, qword ptr gs:[0x188]
00316F53  48 8D 45 B0                     lea rax, [rbp - 0x50]
00316F57  83 65 AC 00                     and dword ptr [rbp - 0x54], 0
00316F5B  48 8D 55 A0                     lea rdx, [rbp - 0x60]
00316F5F  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
00316F63  41 B8 01 00 00 00               mov r8d, 1
00316F69  48 8D 45 B0                     lea rax, [rbp - 0x50]
00316F6D  44 89 45 F0                     mov dword ptr [rbp - 0x10], r8d
00316F71  48 8B CF                        mov rcx, rdi
00316F74  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
00316F78  66 C7 45 A8 07 01               mov word ptr [rbp - 0x58], 0x107
00316F7E  C6 45 AA 06                     mov byte ptr [rbp - 0x56], 6
00316F82  E8 ED 9E 11 00                  call 0x140430e74
00316F87  48 8B D7                        mov rdx, rdi
00316F8A  48 8B CB                        mov rcx, rbx
00316F8D  E8 36 EA F8 FF                  call 0x1402a59c8
00316F92  45 33 C0                        xor r8d, r8d
00316F95  48 8D 4D A8                     lea rcx, [rbp - 0x58]
00316F99  41 8D 50 12                     lea edx, [r8 + 0x12]
00316F9D  E8 F2 37 FB FF                  call 0x1402ca794
00316FA2  48 8B D7                        mov rdx, rdi
00316FA5  48 8B CB                        mov rcx, rbx
00316FA8  E8 63 E8 F7 FF                  call 0x140295810
00316FAD  4C 8D 9C 24 80 00 00 00         lea r11, [rsp + 0x80]
00316FB5  49 8B 5B 10                     mov rbx, qword ptr [r11 + 0x10]
00316FB9  49 8B 7B 18                     mov rdi, qword ptr [r11 + 0x18]
00316FBD  49 8B E3                        mov rsp, r11
00316FC0  5D                              pop rbp
00316FC1  C3                              ret
00316FC2  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiWaitForVadDeletion(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned int v_stack_m18;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned __int8 v_stack_m5E;
    unsigned __int16 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rdi;
    v_rsp = (v_rsp) - (128);
    a2 = 0;
    result = memset(v_stack_m68, a2, a2 + 88, a4);
    if ((*(unsigned __int64 *)(a1 + 16)) != -1) {
        v_rbx = *(unsigned __int64 *)(gs_base + (0 + 392));
        result = v_stack_m58;
        a2 = v_stack_m68;
        v_stack_m50 = result;
        a3 = 1;
        result = v_stack_m58;
        v_stack_m18 = (unsigned int)(a3);
        a1 = a1;
        v_stack_m58 = result;
        v_stack_m60 = 263;
        v_stack_m5E = 6;
        result = MiInsertVadEvent(a1, a2, a3, a4);
        a2 = a1;
        a1 = v_rbx;
        result = MiUnlockVad(a1, a2, a3, a4);
        a3 = 0;
        a1 = v_stack_m60;
        a2 = a3 + 18;
        result = KeWaitForGate(a1, a2, a3, a4);
        a2 = a1;
        a1 = v_rbx;
        result = MiLockVad(a1, a2, a3, a4);
    }
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiWaitForVadDeletion(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint32_t v_stack_m18;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint8_t v_stack_m5E;
    uint16_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rdi;
    local_rsp = (local_rsp) - (128);
    Arg2 = 0;
    result = memset(v_stack_m68, Arg2, Arg2 + 88, a4);
    if ((*(uint64_t *)(arg1 + 0x10)) != -1) {
        local_rbx = *(uint64_t *)(gs_base + (0 + 0x188));
        result = v_stack_m58;
        Arg2 = v_stack_m68;
        v_stack_m50 = result;
        a3 = 1;
        result = v_stack_m58;
        v_stack_m18 = (uint32_t)(a3);
        Arg1 = Arg1;
        v_stack_m58 = result;
        v_stack_m60 = 263;
        v_stack_m5E = 6;
        result = MiInsertVadEvent(Arg1, Arg2, a3, a4);
        Arg2 = Arg1;
        Arg1 = local_rbx;
        result = MiUnlockVad(Arg1, Arg2, a3, a4);
        a3 = 0;
        Arg1 = v_stack_m60;
        Arg2 = a3 + 18;
        result = KeWaitForGate(Arg1, Arg2, a3, a4);
        Arg2 = Arg1;
        Arg1 = local_rbx;
        result = MiLockVad(Arg1, Arg2, a3, a4);
    }
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00316F1C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00316F1C[BB_00316F1C]
  bb_00316F4A[BB_00316F4A]
  bb_00316FAD[BB_00316FAD]
  bb_00316FC2[BB_00316FC2]
  bb_00316F1C -->|branch| bb_00316FAD
  bb_00316F1C -->|fallthrough| bb_00316F4A
  bb_00316F4A -->|flow| bb_00316FAD
```
