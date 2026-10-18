# BiSetObjectDescription

- RVA: `0x00A41DE8`–`0x00A41E6B` (길이 `131` bytes)
- VA: `0x0000000140A41DE8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00084AC0`
- 디코드: `32`개 명령, `131/131` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00A41E22` → [BiCreateKey](BiCreateKey_function_00A404DC.md) (function, `0x00A404DC`)
- `0x00A41E30` → [BiCloseKey](../91/BiCloseKey_function_00916A00.md) (function, `0x00916A00`)
- `0x00A41E5A` → [BiSetRegistryValue](../A3/BiSetRegistryValue_function_00A3E3B0.md) (function, `0x00A3E3B0`)

### Direct callers
- [sub_00B3A518](../B3/Unknown_function_00B3A518.md) at `0x00B3A58D`

### Static image references
- `0x00A41E18` → RVA `0x00AFF1D0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00A41E4B` → RVA `0x00AFC720` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A41DE8  4C 8B DC                        mov r11, rsp
00A41DEB  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00A41DEF  57                              push rdi
00A41DF0  48 83 EC 30                     sub rsp, 0x30
00A41DF4  49 83 63 20 00                  and qword ptr [r11 + 0x20], 0
00A41DF9  49 8D 43 18                     lea rax, [r11 + 0x18]
00A41DFD  49 89 43 F0                     mov qword ptr [r11 - 0x10], rax
00A41E01  48 8B FA                        mov rdi, rdx
00A41E04  49 8D 43 20                     lea rax, [r11 + 0x20]
00A41E08  41 B9 01 00 00 00               mov r9d, 1
00A41E0E  41 B8 19 00 02 00               mov r8d, 0x20019
00A41E14  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
00A41E18  48 8D 15 B1 D3 0B 00            lea rdx, [rip + 0xbd3b1]
00A41E1F  48 8B D9                        mov rbx, rcx
00A41E22  E8 B5 E6 FF FF                  call 0x140a404dc
00A41E27  85 C0                           test eax, eax
00A41E29  78 34                           js 0x140a41e5f
00A41E2B  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00A41E30  E8 CB 4B ED FF                  call 0x140916a00
00A41E35  41 B9 04 00 00 00               mov r9d, 4
00A41E3B  48 8D 47 04                     lea rax, [rdi + 4]
00A41E3F  44 89 4C 24 28                  mov dword ptr [rsp + 0x28], r9d
00A41E44  4C 8D 05 85 D3 0B 00            lea r8, [rip + 0xbd385]
00A41E4B  48 8D 15 CE A8 0B 00            lea rdx, [rip + 0xba8ce]
00A41E52  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A41E57  48 8B CB                        mov rcx, rbx
00A41E5A  E8 51 C5 FF FF                  call 0x140a3e3b0
00A41E5F  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00A41E64  48 83 C4 30                     add rsp, 0x30
00A41E68  5F                              pop rdi
00A41E69  C3                              ret
00A41E6A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall BiSetObjectDescription(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    v_rsp = (v_rsp) - (48);
    *(unsigned __int64 *)(v_rsp - 16) = v_rsp + 24;
    *(unsigned __int64 *)(v_rsp - 24) = v_rsp + 32;
    result = BiCreateKey(a1, v_rip + 775089, (unsigned int)(0x20019ULL), 1);
    if (!(sign_flag)) {
        a1 = v_stack_p20;
        result = BiCloseKey(a1, v_rip + 775089, (unsigned int)(0x20019ULL), 1);
        a4 = 4;
        result = a2 + 4;
        v_stack_m10 = (unsigned int)(a4);
        a3 = v_rip + 775045;
        a2 = v_rip + 764110;
        v_stack_m18 = result;
        a1 = a1;
        result = BiSetRegistryValue(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t BiSetObjectDescription(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m10;
    uint64_t v_stack_m18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    local_rsp = (local_rsp) - (48);
    *(uint64_t *)(local_rsp - 0x10) = local_rsp + 24;
    *(uint64_t *)(local_rsp - 0x18) = local_rsp + 32;
    result = BiCreateKey(Arg1, v_rip + 775089, (uint32_t)(0x20019ULL), 1);
    if (!(sign_flag)) {
        Arg1 = v_stack_p20;
        result = BiCloseKey(Arg1, v_rip + 775089, (uint32_t)(0x20019ULL), 1);
        a4 = 4;
        result = Arg2 + 4;
        v_stack_m10 = (uint32_t)(a4);
        a3 = v_rip + 775045;
        Arg2 = v_rip + 764110;
        v_stack_m18 = result;
        Arg1 = Arg1;
        result = BiSetRegistryValue(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (48);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x4` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A41DE8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A41DE8[BB_00A41DE8]
  bb_00A41E2B[BB_00A41E2B]
  bb_00A41E5F[BB_00A41E5F]
  bb_00A41E6A[BB_00A41E6A]
  bb_00A41DE8 -->|branch| bb_00A41E5F
  bb_00A41DE8 -->|fallthrough| bb_00A41E2B
  bb_00A41E2B -->|flow| bb_00A41E5F
```
