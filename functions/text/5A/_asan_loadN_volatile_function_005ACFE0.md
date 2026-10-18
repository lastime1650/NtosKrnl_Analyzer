# _asan_loadN_volatile

- RVA: `0x005ACFE0`–`0x005AD0C3` (길이 `227` bytes)
- VA: `0x00000001405ACFE0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000794E0`
- 디코드: `62`개 명령, `227/227` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x005AD08E` → [KasaniReport](KasaniReport_function_005AB0B0.md) (function, `0x005AB0B0`)
- `0x005AD0AD` → [KcsanValidateAddress](KcsanValidateAddress_function_005AF5E0.md) (function, `0x005AF5E0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x005ACFEF` → RVA `0x00FCEC6A` (`ALMOSTRO`; read)
- `0x005AD040` → RVA `0x00FC6ED8` (`ALMOSTRO`; read)
- `0x005AD093` → RVA `0x00F8A7E8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005ACFE0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
005ACFE5  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
005ACFEA  57                              push rdi
005ACFEB  48 83 EC 30                     sub rsp, 0x30
005ACFEF  80 3D 74 1C A2 00 00            cmp byte ptr [rip + 0xa21c74], 0
005ACFF6  48 8B FA                        mov rdi, rdx
005ACFF9  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
005ACFFE  48 8B D9                        mov rbx, rcx
005AD001  0F 84 AB 00 00 00               je 0x1405ad0b2
005AD007  48 B8 00 00 00 00 00 80 FF FF   movabs rax, 0xffff800000000000
005AD011  48 3B C8                        cmp rcx, rax
005AD014  0F 82 98 00 00 00               jb 0x1405ad0b2
005AD01A  48 85 D2                        test rdx, rdx
005AD01D  74 74                           je 0x1405ad093
005AD01F  48 BA 00 00 00 00 00 80 00 00   movabs rdx, 0x800000000000
005AD029  49 B8 FF FF FF FF FF 7F 00 00   movabs r8, 0x7fffffffffff
005AD033  48 03 D1                        add rdx, rcx
005AD036  4C 03 C1                        add r8, rcx
005AD039  48 C1 EA 03                     shr rdx, 3
005AD03D  4C 03 C7                        add r8, rdi
005AD040  48 03 15 91 9E A1 00            add rdx, qword ptr [rip + 0xa19e91]
005AD047  49 C1 E8 03                     shr r8, 3
005AD04B  4C 03 05 86 9E A1 00            add r8, qword ptr [rip + 0xa19e86]
005AD052  0F B6 0A                        movzx ecx, byte ptr [rdx]
005AD055  49 3B D0                        cmp rdx, r8
005AD058  73 0E                           jae 0x1405ad068
005AD05A  84 C9                           test cl, cl
005AD05C  74 05                           je 0x1405ad063
005AD05E  80 F9 08                        cmp cl, 8
005AD061  7C 1B                           jl 0x1405ad07e
005AD063  48 FF C2                        inc rdx
005AD066  EB EA                           jmp 0x1405ad052
005AD068  84 C9                           test cl, cl
005AD06A  74 27                           je 0x1405ad093
005AD06C  80 F9 08                        cmp cl, 8
005AD06F  7D 22                           jge 0x1405ad093
005AD071  8D 47 FF                        lea eax, [rdi - 1]
005AD074  02 C3                           add al, bl
005AD076  24 07                           and al, 7
005AD078  FE C0                           inc al
005AD07A  3A C1                           cmp al, cl
005AD07C  7E 15                           jle 0x1405ad093
005AD07E  88 4C 24 20                     mov byte ptr [rsp + 0x20], cl
005AD082  4C 8B CE                        mov r9, rsi
005AD085  48 8B CB                        mov rcx, rbx
005AD088  45 33 C0                        xor r8d, r8d
005AD08B  48 8B D7                        mov rdx, rdi
005AD08E  E8 1D E0 FF FF                  call 0x1405ab0b0
005AD093  80 3D 4E D7 9D 00 00            cmp byte ptr [rip + 0x9dd74e], 0
005AD09A  74 16                           je 0x1405ad0b2
005AD09C  41 B1 01                        mov r9b, 1
005AD09F  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
005AD0A4  45 33 C0                        xor r8d, r8d
005AD0A7  48 8B D7                        mov rdx, rdi
005AD0AA  48 8B CB                        mov rcx, rbx
005AD0AD  E8 2E 25 00 00                  call 0x1405af5e0
005AD0B2  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
005AD0B7  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
005AD0BC  48 83 C4 30                     add rsp, 0x30
005AD0C0  5F                              pop rdi
005AD0C1  C3                              ret
005AD0C2  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall _asan_loadN_volatile(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int8 v_stack_m18;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (48);
    if ((*(unsigned __int8 *)(v_rip + 10624116)) == 0) goto loc_005AD0B2;
    if (a1 < result) goto loc_005AD0B2;
    if (a2 == 0) goto loc_005AD093;
    a2 = (a2) + (a1);
    a3 = (a3) + (a1);
    a2 = (a2) >> (3);
    a3 = (a3) + (a2);
    a2 = (a2) + (*(unsigned __int64 *)(v_rip + 10591889));
    a3 = (a3) >> (3);
    a3 = (a3) + (*(unsigned __int64 *)(v_rip + 10591878));
loc_005AD052:
    if (a2 >= a3) goto loc_005AD068;
    if ((unsigned __int8)(*(unsigned __int8 *)(a2)) == 0) goto loc_005AD063;
    if (((unsigned __int8)(*(unsigned __int8 *)(a2))) < 8) goto loc_005AD07E;
loc_005AD063:
    a2 = (a2) + 1;
    goto loc_005AD052;
loc_005AD068:
    if ((unsigned __int8)(*(unsigned __int8 *)(a2)) == 0) goto loc_005AD093;
    if (((unsigned __int8)(*(unsigned __int8 *)(a2))) >= 8) goto loc_005AD093;
    result = (unsigned __int8)((a2 - 1) + ((unsigned __int8)(a1)));
    result = (unsigned __int8)((result) & (7));
    result = (unsigned __int8)((result) + 1);
    if (((unsigned __int8)(result)) >= = ((unsigned __int8)(*(unsigned __int8 *)(a2)))) {
        v_stack_m18 = (unsigned __int8)(*(unsigned __int8 *)(a2));
        a4 = v_stack_p0;
        a1 = a1;
        a3 = 0;
        a2 = a2;
        result = KasaniReport(a1, a2, a3, a4);
    }
    if ((*(unsigned __int8 *)(v_rip + 10344270)) != 0) {
        a4 = 1;
        v_stack_m18 = v_stack_p0;
        a3 = 0;
        a2 = a2;
        a1 = a1;
        result = KcsanValidateAddress(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t _asan_loadN_volatile(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint8_t v_stack_m18;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (48);
    if ((*(uint8_t *)(v_rip + 0xA21C74)) == 0) goto loc_005AD0B2;
    if (Arg1 < result) goto loc_005AD0B2;
    if (Arg2 == NULL) goto loc_005AD093;
    Arg2 = (Arg2) + (Arg1);
    a3 = (a3) + (Arg1);
    Arg2 = (Arg2) >> (3);
    a3 = (a3) + (Arg2);
    Arg2 = (Arg2) + (*(uint64_t *)(v_rip + 0xA19E91));
    a3 = (a3) >> (3);
    a3 = (a3) + (*(uint64_t *)(v_rip + 0xA19E86));
loc_005AD052:
    if (Arg2 >= a3) goto loc_005AD068;
    if ((uint8_t)(*(uint8_t *)(arg2)) == 0) goto loc_005AD063;
    if (((uint8_t)(*(uint8_t *)(arg2))) < 8) goto loc_005AD07E;
loc_005AD063:
    Arg2 = (Arg2) + 1;
    goto loc_005AD052;
loc_005AD068:
    if ((uint8_t)(*(uint8_t *)(arg2)) == 0) goto loc_005AD093;
    if (((uint8_t)(*(uint8_t *)(arg2))) >= 8) goto loc_005AD093;
    result = (uint8_t)((Arg2 - 1) + ((uint8_t)(Arg1)));
    result = (uint8_t)((result) & (7));
    result = (uint8_t)((result) + 1);
    if (((uint8_t)(result)) >= = ((uint8_t)(*(uint8_t *)(arg2)))) {
        v_stack_m18 = (uint8_t)(*(uint8_t *)(arg2));
        a4 = v_stack_p0;
        Arg1 = Arg1;
        a3 = 0;
        Arg2 = Arg2;
        result = KasaniReport(Arg1, Arg2, a3, a4);
    }
    if ((*(uint8_t *)(v_rip + 0x9DD74E)) != 0) {
        a4 = 1;
        v_stack_m18 = v_stack_p0;
        a3 = 0;
        Arg2 = Arg2;
        Arg1 = Arg1;
        result = KcsanValidateAddress(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (48);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `- 0x1` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005ACFE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005ACFE0[BB_005ACFE0]
  bb_005AD007[BB_005AD007]
  bb_005AD01A[BB_005AD01A]
  bb_005AD01F[BB_005AD01F]
  bb_005AD052[BB_005AD052]
  bb_005AD05A[BB_005AD05A]
  bb_005AD05E[BB_005AD05E]
  bb_005AD063[BB_005AD063]
  bb_005AD068[BB_005AD068]
  bb_005AD06C[BB_005AD06C]
  bb_005AD071[BB_005AD071]
  bb_005AD07E[BB_005AD07E]
  bb_005AD093[BB_005AD093]
  bb_005AD09C[BB_005AD09C]
  bb_005AD0B2[BB_005AD0B2]
  bb_005AD0C2[BB_005AD0C2]
  bb_005ACFE0 -->|branch| bb_005AD0B2
  bb_005ACFE0 -->|fallthrough| bb_005AD007
  bb_005AD007 -->|branch| bb_005AD0B2
  bb_005AD007 -->|fallthrough| bb_005AD01A
  bb_005AD01A -->|branch| bb_005AD093
  bb_005AD01A -->|fallthrough| bb_005AD01F
  bb_005AD01F -->|flow| bb_005AD052
  bb_005AD052 -->|branch| bb_005AD068
  bb_005AD052 -->|fallthrough| bb_005AD05A
  bb_005AD05A -->|branch| bb_005AD063
  bb_005AD05A -->|fallthrough| bb_005AD05E
  bb_005AD05E -->|branch| bb_005AD07E
  bb_005AD05E -->|fallthrough| bb_005AD063
  bb_005AD063 -->|branch| bb_005AD052
  bb_005AD068 -->|branch| bb_005AD093
  bb_005AD068 -->|fallthrough| bb_005AD06C
  bb_005AD06C -->|branch| bb_005AD093
  bb_005AD06C -->|fallthrough| bb_005AD071
  bb_005AD071 -->|branch| bb_005AD093
  bb_005AD071 -->|fallthrough| bb_005AD07E
  bb_005AD07E -->|flow| bb_005AD093
  bb_005AD093 -->|branch| bb_005AD0B2
  bb_005AD093 -->|fallthrough| bb_005AD09C
  bb_005AD09C -->|flow| bb_005AD0B2
```
