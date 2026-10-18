# IommupHvMapDeviceLogicalRange

- RVA: `0x00306C94`–`0x00306D3E` (길이 `170` bytes)
- VA: `0x0000000140306C94`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000737F8`
- 디코드: `48`개 명령, `170/170` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00306CF0` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00306D0F` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00306D2D` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [HalpIommuDomainUnmapLogicalRange](HalpIommuDomainUnmapLogicalRange_function_00307258.md) at `0x003072FF`
- [HalpIommuDomainMapLogicalRange](../55/HalpIommuDomainMapLogicalRange_function_00555064.md) at `0x00555081`

### Static image references
- `0x00306CD0` → RVA `0x00FC1E28` (`.data`; read)
- `0x00306CFB` → RVA `0x00FC1E30` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00306C94  4C 8B DC                        mov r11, rsp
00306C97  53                              push rbx
00306C98  56                              push rsi
00306C99  57                              push rdi
00306C9A  48 83 EC 40                     sub rsp, 0x40
00306C9E  8B 41 30                        mov eax, dword ptr [rcx + 0x30]
00306CA1  48 8B F1                        mov rsi, rcx
00306CA4  49 83 63 08 00                  and qword ptr [r11 + 8], 0
00306CA9  49 8D 4B 18                     lea rcx, [r11 + 0x18]
00306CAD  48 8B 9C 24 80 00 00 00         mov rbx, qword ptr [rsp + 0x80]
00306CB5  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
00306CB9  49 8D 81 FF 0F 00 00            lea rax, [r9 + 0xfff]
00306CC0  48 C1 E8 0C                     shr rax, 0xc
00306CC4  4D 8D 4B 20                     lea r9, [r11 + 0x20]
00306CC8  49 C1 E8 0C                     shr r8, 0xc
00306CCC  49 89 43 18                     mov qword ptr [r11 + 0x18], rax
00306CD0  48 8B 05 51 B1 CB 00            mov rax, qword ptr [rip + 0xcbb151]
00306CD7  4D 89 43 20                     mov qword ptr [r11 + 0x20], r8
00306CDB  4C 8B C3                        mov r8, rbx
00306CDE  C6 44 24 28 01                  mov byte ptr [rsp + 0x28], 1
00306CE3  49 89 4B C8                     mov qword ptr [r11 - 0x38], rcx
00306CE7  49 8D 4B 08                     lea rcx, [r11 + 8]
00306CEB  C6 44 24 64 00                  mov byte ptr [rsp + 0x64], 0
00306CF0  E8 DB 3D 3B 00                  call 0x1406baad0
00306CF5  8B F8                           mov edi, eax
00306CF7  85 C0                           test eax, eax
00306CF9  79 38                           jns 0x140306d33
00306CFB  48 8B 05 2E B1 CB 00            mov rax, qword ptr [rip + 0xcbb12e]
00306D02  4C 8D 44 24 70                  lea r8, [rsp + 0x70]
00306D07  48 8B D3                        mov rdx, rbx
00306D0A  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
00306D0F  E8 BC 3D 3B 00                  call 0x1406baad0
00306D14  85 C0                           test eax, eax
00306D16  79 1B                           jns 0x140306d33
00306D18  4C 63 C0                        movsxd r8, eax
00306D1B  4C 8B CE                        mov r9, rsi
00306D1E  BA 01 00 00 00                  mov edx, 1
00306D23  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00306D28  B9 D9 01 00 00                  mov ecx, 0x1d9
00306D2D  E8 2E 69 1F 00                  call 0x1404fd660
00306D32  CC                              int3
00306D33  8B C7                           mov eax, edi
00306D35  48 83 C4 40                     add rsp, 0x40
00306D39  5F                              pop rdi
00306D3A  5E                              pop rsi
00306D3B  5B                              pop rbx
00306D3C  C3                              ret
00306D3D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IommupHvMapDeviceLogicalRange(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int8 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p8;
    unsigned __int8 v_stack_pC;

    v_rsp = (v_rsp) - (64);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48)));
    result = (a4 + 4095) >> (12);
    a3 = (a3) >> (12);
    *(unsigned __int64 *)(v_rsp + 24) = result;
    *(unsigned __int64 *)(v_rsp + 32) = a3;
    v_stack_m30 = 1;
    *(unsigned __int64 *)(v_rsp - 56) = v_rsp + 24;
    v_stack_pC = 0;
    result = guard_dispatch_icall(v_rsp + 8, a2, a5, v_rsp + 32);
    if (!sign_flag) goto loc_00306D33;
    result = guard_dispatch_icall(v_stack_p8, a5, v_stack_p18, v_rsp + 32);
    if (sign_flag) {
        a3 = (int)((unsigned int)(result));
        a4 = a1;
        a2 = 1;
        v_stack_m38 = a5;
        a1 = 473;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
}
```

## 5. (Beta) C Style

```c
int64_t IommupHvMapDeviceLogicalRange(void *Arg1, int64_t Arg2, int64_t Arg3, void *Arg4, int64_t Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_rsp;
    uint8_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_p18;
    uint32_t v_stack_p8;
    uint8_t v_stack_pC;

    local_rsp = (local_rsp) - (64);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30)));
    result = (Arg4 + 4095) >> (12);
    Arg3 = (Arg3) >> (12);
    *(uint64_t *)(local_rsp + 0x18) = result;
    *(uint64_t *)(local_rsp + 0x20) = Arg3;
    v_stack_m30 = 1;
    *(uint64_t *)(local_rsp - 0x38) = local_rsp + 24;
    v_stack_pC = 0;
    result = guard_dispatch_icall(local_rsp + 8, Arg2, Arg5, local_rsp + 32);
    if (!sign_flag) goto loc_00306D33;
    result = guard_dispatch_icall(v_stack_p8, Arg5, v_stack_p18, local_rsp + 32);
    if (sign_flag) {
        Arg3 = (int32_t)((uint32_t)(result));
        Arg4 = Arg1;
        Arg2 = 1;
        v_stack_m38 = Arg5;
        Arg1 = 473;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, Arg4);
    }
    local_rsp = (local_rsp) + (64);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x30` | `32` | `R` |
| `Arg4` | `+ 0xFFF` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00306C94&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00306C94[BB_00306C94]
  bb_00306CFB[BB_00306CFB]
  bb_00306D18[BB_00306D18]
  bb_00306D33[BB_00306D33]
  bb_00306D3D[BB_00306D3D]
  bb_00306C94 -->|branch| bb_00306D33
  bb_00306C94 -->|fallthrough| bb_00306CFB
  bb_00306CFB -->|branch| bb_00306D33
  bb_00306CFB -->|fallthrough| bb_00306D18
  bb_00306D18 -->|flow| bb_00306D33
```
