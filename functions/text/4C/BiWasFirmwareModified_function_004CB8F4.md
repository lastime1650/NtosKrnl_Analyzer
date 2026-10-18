# BiWasFirmwareModified

- RVA: `0x004CB8F4`–`0x004CB95B` (길이 `103` bytes)
- VA: `0x00000001404CB8F4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00084AC0`
- 디코드: `29`개 명령, `103/103` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x004CB92C` → [BiGetRegistryValue](../../page/A3/BiGetRegistryValue_function_00A3F3CC.md) (function, `0x00A3F3CC`)
- `0x004CB941` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [BiCloseStore](../../page/A3/BiCloseStore_function_00A3C5D8.md) at `0x00A3C5FB`
- [BiOpenSystemStore](../../page/A4/BiOpenSystemStore_function_00A40844.md) at `0x00A4098F`

### Static image references
- `0x004CB90A` → RVA `0x006D0A20` (` ?? ::FNODOBFM::`string'`; read)
- `0x004CB919` → RVA `0x006D0A40` (` ?? ::FNODOBFM::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x004CB92C` → [BiGetRegistryValue](../../page/A3/BiGetRegistryValue_function_00A3F3CC.md) (`.text` → `PAGE`)
  - `0x004CB941` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004CB8F4  4C 8B DC                        mov r11, rsp
004CB8F7  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
004CB8FB  57                              push rdi
004CB8FC  48 83 EC 30                     sub rsp, 0x30
004CB900  33 FF                           xor edi, edi
004CB902  49 8D 43 10                     lea rax, [r11 + 0x10]
004CB906  49 89 43 F0                     mov qword ptr [r11 - 0x10], rax
004CB90A  4C 8D 05 0F 51 20 00            lea r8, [rip + 0x20510f]
004CB911  49 8D 43 18                     lea rax, [r11 + 0x18]
004CB915  49 89 7B 18                     mov qword ptr [r11 + 0x18], rdi
004CB919  48 8D 15 20 51 20 00            lea rdx, [rip + 0x205120]
004CB920  89 7C 24 48                     mov dword ptr [rsp + 0x48], edi
004CB924  44 8D 4F 04                     lea r9d, [rdi + 4]
004CB928  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
004CB92C  E8 9B 3A 57 00                  call 0x140a3f3cc
004CB931  85 C0                           test eax, eax
004CB933  78 17                           js 0x1404cb94c
004CB935  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
004CB93A  BA 42 43 44 4B                  mov edx, 0x4b444342
004CB93F  8B 19                           mov ebx, dword ptr [rcx]
004CB941  E8 2A 6F 6B 00                  call 0x140b82870
004CB946  85 DB                           test ebx, ebx
004CB948  40 0F 95 C7                     setne dil
004CB94C  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
004CB951  40 8A C7                        mov al, dil
004CB954  48 83 C4 30                     add rsp, 0x30
004CB958  5F                              pop rdi
004CB959  C3                              ret
004CB95A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall BiWasFirmwareModified(void)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    v_rsp = (v_rsp) - (48);
    v_rdi = 0;
    *(unsigned __int64 *)(v_rsp - 16) = v_rsp + 16;
    *(unsigned __int64 *)(v_rsp + 24) = 0;
    v_stack_p10 = 0;
    *(unsigned __int64 *)(v_rsp - 24) = v_rsp + 24;
    result = BiGetRegistryValue(a1, v_rip + 2117920, v_rip + 2117903, v_rdi + 4);
    if (!(sign_flag)) {
        a1 = v_stack_p18;
        a2 = 0x4B444342ULL;
        v_rbx = *(unsigned int *)(a1);
        result = ExFreePoolWithTag(a1, a2, v_rip + 2117903, v_rdi + 4);
        v_rdi = ((unsigned int)(v_rbx) != 0) ? 1 : 0;
    }
    v_rsp = (v_rsp) + (48);
    return (unsigned __int8)(v_rdi);
}
```

## 5. (Beta) C Style

```c
void BiWasFirmwareModified(void)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint32_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    local_rsp = (local_rsp) - (48);
    local_rdi = 0;
    *(uint64_t *)(local_rsp - 0x10) = local_rsp + 16;
    *(uint64_t *)(local_rsp + 0x18) = 0;
    v_stack_p10 = 0;
    *(uint64_t *)(local_rsp - 0x18) = local_rsp + 24;
    result = BiGetRegistryValue(a1, v_rip + 2117920, v_rip + 2117903, local_rdi + 4);
    if (!(sign_flag)) {
        a1 = v_stack_p18;
        a2 = 0x4B444342ULL;
        local_rbx = *(uint32_t *)(a1);
        result = ExFreePoolWithTag(a1, a2, v_rip + 2117903, local_rdi + 4);
        local_rdi = ((uint32_t)(local_rbx) != 0) ? 1 : 0;
    }
    local_rsp = (local_rsp) + (48);
    return (uint8_t)(local_rdi);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004CB8F4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004CB8F4[BB_004CB8F4]
  bb_004CB935[BB_004CB935]
  bb_004CB94C[BB_004CB94C]
  bb_004CB95A[BB_004CB95A]
  bb_004CB8F4 -->|branch| bb_004CB94C
  bb_004CB8F4 -->|fallthrough| bb_004CB935
  bb_004CB935 -->|flow| bb_004CB94C
```
