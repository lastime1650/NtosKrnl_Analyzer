# _asan_load2

- RVA: `0x005AC830`–`0x005AC90D` (길이 `221` bytes)
- VA: `0x00000001405AC830`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006E5F8`
- 디코드: `64`개 명령, `221/221` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x005AC8DC` → [KasaniReport](KasaniReport_function_005AB0B0.md) (function, `0x005AB0B0`)
- `0x005AC8FC` → [KcsanValidateAddress](KcsanValidateAddress_function_005AF5E0.md) (function, `0x005AF5E0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x005AC83A` → RVA `0x00FCEC6A` (`ALMOSTRO`; read)
- `0x005AC862` → RVA `0x00FC6ED8` (`ALMOSTRO`; read)
- `0x005AC8E1` → RVA `0x00F8A7E8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005AC830  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
005AC835  57                              push rdi
005AC836  48 83 EC 30                     sub rsp, 0x30
005AC83A  80 3D 29 24 A2 00 00            cmp byte ptr [rip + 0xa22429], 0
005AC841  48 8B D9                        mov rbx, rcx
005AC844  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
005AC849  0F 84 B2 00 00 00               je 0x1405ac901
005AC84F  48 B8 00 00 00 00 00 80 FF FF   movabs rax, 0xffff800000000000
005AC859  48 3B C8                        cmp rcx, rax
005AC85C  0F 82 9F 00 00 00               jb 0x1405ac901
005AC862  4C 8B 05 6F A6 A1 00            mov r8, qword ptr [rip + 0xa1a66f]
005AC869  49 B9 00 00 00 00 00 80 00 00   movabs r9, 0x800000000000
005AC873  4A 8D 04 09                     lea rax, [rcx + r9]
005AC877  48 C1 E8 03                     shr rax, 3
005AC87B  42 0F B6 0C 00                  movzx ecx, byte ptr [rax + r8]
005AC880  8B C3                           mov eax, ebx
005AC882  83 E0 07                        and eax, 7
005AC885  3C 06                           cmp al, 6
005AC887  76 2E                           jbe 0x1405ac8b7
005AC889  84 C9                           test cl, cl
005AC88B  74 05                           je 0x1405ac892
005AC88D  80 F9 08                        cmp cl, 8
005AC890  7C 39                           jl 0x1405ac8cb
005AC892  48 8D 53 01                     lea rdx, [rbx + 1]
005AC896  4A 8D 04 0A                     lea rax, [rdx + r9]
005AC89A  48 C1 E8 03                     shr rax, 3
005AC89E  42 0F B6 0C 00                  movzx ecx, byte ptr [rax + r8]
005AC8A3  84 C9                           test cl, cl
005AC8A5  74 3A                           je 0x1405ac8e1
005AC8A7  80 F9 08                        cmp cl, 8
005AC8AA  7D 35                           jge 0x1405ac8e1
005AC8AC  80 E2 07                        and dl, 7
005AC8AF  FE C2                           inc dl
005AC8B1  3A D1                           cmp dl, cl
005AC8B3  7E 2C                           jle 0x1405ac8e1
005AC8B5  EB 14                           jmp 0x1405ac8cb
005AC8B7  84 C9                           test cl, cl
005AC8B9  74 26                           je 0x1405ac8e1
005AC8BB  80 F9 08                        cmp cl, 8
005AC8BE  7D 21                           jge 0x1405ac8e1
005AC8C0  8D 43 01                        lea eax, [rbx + 1]
005AC8C3  24 07                           and al, 7
005AC8C5  FE C0                           inc al
005AC8C7  3A C1                           cmp al, cl
005AC8C9  7E 16                           jle 0x1405ac8e1
005AC8CB  45 33 C0                        xor r8d, r8d
005AC8CE  88 4C 24 20                     mov byte ptr [rsp + 0x20], cl
005AC8D2  4C 8B CF                        mov r9, rdi
005AC8D5  48 8B CB                        mov rcx, rbx
005AC8D8  41 8D 50 02                     lea edx, [r8 + 2]
005AC8DC  E8 CF E7 FF FF                  call 0x1405ab0b0
005AC8E1  80 3D 00 DF 9D 00 00            cmp byte ptr [rip + 0x9ddf00], 0
005AC8E8  74 17                           je 0x1405ac901
005AC8EA  45 33 C9                        xor r9d, r9d
005AC8ED  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
005AC8F2  45 33 C0                        xor r8d, r8d
005AC8F5  48 8B CB                        mov rcx, rbx
005AC8F8  41 8D 51 02                     lea edx, [r9 + 2]
005AC8FC  E8 DF 2C 00 00                  call 0x1405af5e0
005AC901  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
005AC906  48 83 C4 30                     add rsp, 0x30
005AC90A  5F                              pop rdi
005AC90B  C3                              ret
005AC90C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall _asan_load2(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int8 v_stack_m18;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (48);
    if ((*(unsigned __int8 *)(v_rip + 10626089)) == 0) goto loc_005AC901;
    if (a1 < result) goto loc_005AC901;
    result = (a1 + a4 * 1) >> (3);
    result = (unsigned int)(((unsigned int)((unsigned int)(a1))) & (7));
    if (((unsigned __int8)(result)) <= 6) goto loc_005AC8B7;
    if ((unsigned __int8)(*(unsigned __int8 *)(result + *(unsigned __int64 *)(v_rip + 10593903) * 1)) == 0) goto loc_005AC892;
    if (((unsigned __int8)(*(unsigned __int8 *)(result + *(unsigned __int64 *)(v_rip + 10593903) * 1))) < 8) goto loc_005AC8CB;
loc_005AC892:
    result = (a1 + 1 + a4 * 1) >> (3);
    if ((unsigned __int8)(*(unsigned __int8 *)(result + *(unsigned __int64 *)(v_rip + 10593903) * 1)) == 0) goto loc_005AC8E1;
    if (((unsigned __int8)(*(unsigned __int8 *)(result + *(unsigned __int64 *)(v_rip + 10593903) * 1))) >= 8) goto loc_005AC8E1;
    a2 = (unsigned __int8)((a1 + 1) & (7));
    a2 = (unsigned __int8)((a2) + 1);
    if (((unsigned __int8)(a2)) <= ((unsigned __int8)(*(unsigned __int8 *)(result + *(unsigned __int64 *)(v_rip + 10593903) * 1)))) goto loc_005AC8E1;
    goto loc_005AC8CB;
loc_005AC8B7:
    if ((unsigned __int8)(*(unsigned __int8 *)(result + *(unsigned __int64 *)(v_rip + 10593903) * 1)) == 0) goto loc_005AC8E1;
    if (((unsigned __int8)(*(unsigned __int8 *)(result + *(unsigned __int64 *)(v_rip + 10593903) * 1))) >= 8) goto loc_005AC8E1;
    result = (unsigned __int8)((a1 + 1) & (7));
    result = (unsigned __int8)((result) + 1);
    if (((unsigned __int8)(result)) >= = ((unsigned __int8)(*(unsigned __int8 *)(result + *(unsigned __int64 *)(v_rip + 10593903) * 1)))) {
        a3 = 0;
        v_stack_m18 = (unsigned __int8)(*(unsigned __int8 *)(result + *(unsigned __int64 *)(v_rip + 10593903) * 1));
        a4 = v_stack_p0;
        a1 = a1;
        a2 = a3 + 2;
        result = KasaniReport(a1, a2, a3, a4);
    }
    if ((*(unsigned __int8 *)(v_rip + 10346240)) != 0) {
        a4 = 0;
        v_stack_m18 = v_stack_p0;
        a3 = 0;
        a1 = a1;
        a2 = a4 + 2;
        result = KcsanValidateAddress(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t _asan_load2(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint8_t v_stack_m18;
    uint64_t v_stack_p0;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (48);
    if ((*(uint8_t *)(v_rip + 0xA22429)) == 0) goto loc_005AC901;
    if (Arg1 < result) goto loc_005AC901;
    result = (Arg1 + a4 * 1) >> (3);
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) & (7));
    if (((uint8_t)(result)) <= 6) goto loc_005AC8B7;
    if ((uint8_t)(*(uint8_t *)(result + *(uint64_t *)(v_rip + 0xA1A66F) * 1)) == 0) goto loc_005AC892;
    if (((uint8_t)(*(uint8_t *)(result + *(uint64_t *)(v_rip + 0xA1A66F) * 1))) < 8) goto loc_005AC8CB;
loc_005AC892:
    result = (Arg1 + 1 + a4 * 1) >> (3);
    if ((uint8_t)(*(uint8_t *)(result + *(uint64_t *)(v_rip + 0xA1A66F) * 1)) == 0) goto loc_005AC8E1;
    if (((uint8_t)(*(uint8_t *)(result + *(uint64_t *)(v_rip + 0xA1A66F) * 1))) >= 8) goto loc_005AC8E1;
    a2 = (uint8_t)((Arg1 + 1) & (7));
    a2 = (uint8_t)((a2) + 1);
    if (((uint8_t)(a2)) <= ((uint8_t)(*(uint8_t *)(result + *(uint64_t *)(v_rip + 0xA1A66F) * 1)))) goto loc_005AC8E1;
    goto loc_005AC8CB;
loc_005AC8B7:
    if ((uint8_t)(*(uint8_t *)(result + *(uint64_t *)(v_rip + 0xA1A66F) * 1)) == 0) goto loc_005AC8E1;
    if (((uint8_t)(*(uint8_t *)(result + *(uint64_t *)(v_rip + 0xA1A66F) * 1))) >= 8) goto loc_005AC8E1;
    result = (uint8_t)((Arg1 + 1) & (7));
    result = (uint8_t)((result) + 1);
    if (((uint8_t)(result)) >= = ((uint8_t)(*(uint8_t *)(result + *(uint64_t *)(v_rip + 0xA1A66F) * 1)))) {
        a3 = 0;
        v_stack_m18 = (uint8_t)(*(uint8_t *)(result + *(uint64_t *)(v_rip + 0xA1A66F) * 1));
        a4 = v_stack_p0;
        Arg1 = Arg1;
        a2 = a3 + 2;
        result = KasaniReport(Arg1, a2, a3, a4);
    }
    if ((*(uint8_t *)(v_rip + 0x9DDF00)) != 0) {
        a4 = 0;
        v_stack_m18 = v_stack_p0;
        a3 = 0;
        Arg1 = Arg1;
        a2 = a4 + 2;
        result = KcsanValidateAddress(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (48);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0 + r9*1` | `64` | `R` |
| `Arg1` | `+ 0x1` | `32` | `R` |
| `Arg1` | `+ 0x1` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005AC830&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005AC830[BB_005AC830]
  bb_005AC84F[BB_005AC84F]
  bb_005AC862[BB_005AC862]
  bb_005AC889[BB_005AC889]
  bb_005AC88D[BB_005AC88D]
  bb_005AC892[BB_005AC892]
  bb_005AC8A7[BB_005AC8A7]
  bb_005AC8AC[BB_005AC8AC]
  bb_005AC8B5[BB_005AC8B5]
  bb_005AC8B7[BB_005AC8B7]
  bb_005AC8BB[BB_005AC8BB]
  bb_005AC8C0[BB_005AC8C0]
  bb_005AC8CB[BB_005AC8CB]
  bb_005AC8E1[BB_005AC8E1]
  bb_005AC8EA[BB_005AC8EA]
  bb_005AC901[BB_005AC901]
  bb_005AC90C[BB_005AC90C]
  bb_005AC830 -->|branch| bb_005AC901
  bb_005AC830 -->|fallthrough| bb_005AC84F
  bb_005AC84F -->|branch| bb_005AC901
  bb_005AC84F -->|fallthrough| bb_005AC862
  bb_005AC862 -->|branch| bb_005AC8B7
  bb_005AC862 -->|fallthrough| bb_005AC889
  bb_005AC889 -->|branch| bb_005AC892
  bb_005AC889 -->|fallthrough| bb_005AC88D
  bb_005AC88D -->|branch| bb_005AC8CB
  bb_005AC88D -->|fallthrough| bb_005AC892
  bb_005AC892 -->|branch| bb_005AC8E1
  bb_005AC892 -->|fallthrough| bb_005AC8A7
  bb_005AC8A7 -->|branch| bb_005AC8E1
  bb_005AC8A7 -->|fallthrough| bb_005AC8AC
  bb_005AC8AC -->|branch| bb_005AC8E1
  bb_005AC8AC -->|fallthrough| bb_005AC8B5
  bb_005AC8B5 -->|branch| bb_005AC8CB
  bb_005AC8B7 -->|branch| bb_005AC8E1
  bb_005AC8B7 -->|fallthrough| bb_005AC8BB
  bb_005AC8BB -->|branch| bb_005AC8E1
  bb_005AC8BB -->|fallthrough| bb_005AC8C0
  bb_005AC8C0 -->|branch| bb_005AC8E1
  bb_005AC8C0 -->|fallthrough| bb_005AC8CB
  bb_005AC8CB -->|flow| bb_005AC8E1
  bb_005AC8E1 -->|branch| bb_005AC901
  bb_005AC8E1 -->|fallthrough| bb_005AC8EA
  bb_005AC8EA -->|flow| bb_005AC901
```
