# SbpWaitForVmbus

- RVA: `0x00C6F8D8`–`0x00C6F986` (길이 `174` bytes)
- VA: `0x0000000140C6F8D8`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007F554`
- 디코드: `39`개 명령, `174/174` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **10**

### Outgoing calls
- `0x00C6F93F` → [IoRegisterPlugPlayNotification](../../page/95/IoRegisterPlugPlayNotification_function_009535A0.md) (function, `0x009535A0`)
- `0x00C6F96C` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x00C6F978` → [IoUnregisterPlugPlayNotification](../../page/AA/IoUnregisterPlugPlayNotification_function_00AA5CC0.md) (function, `0x00AA5CC0`)

### Direct callers
- [IopInitializeBootDrivers](../C2/IopInitializeBootDrivers_function_00C2E6F4.md) at `0x00C2EF3C`

### Static image references
- `0x00C6F8E0` → RVA `0x00F8C440` (`.data`; read)
- `0x00C6F8E7` → RVA `0x00EF0288` (`.data`; read)
- `0x00C6F8F3` → RVA `0x00042BC8` (`.rdata`; read)
- `0x00C6F8FA` → RVA `0x00EF0284` (`.data`; read/write)
- `0x00C6F906` → RVA `0x00EF0290` (`.data`; write)
- `0x00C6F90D` → RVA `0x00EF0288` (`.data`; write)
- `0x00C6F91C` → RVA `0x0083C520` (`SbpVmbusNotificationHandler`; read)
- `0x00C6F92F` → RVA `0x00EF0280` (`.data`; write)
- `0x00C6F938` → RVA `0x00EF0282` (`.data`; write)
- `0x00C6F963` → RVA `0x00EF0280` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00C6F93F` → [IoRegisterPlugPlayNotification](../../page/95/IoRegisterPlugPlayNotification_function_009535A0.md) (`INIT` → `PAGE`)
  - `0x00C6F96C` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (`INIT` → `.text`)
  - `0x00C6F978` → [IoUnregisterPlugPlayNotification](../../page/AA/IoUnregisterPlugPlayNotification_function_00AA5CC0.md) (`INIT` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C6F8D8  4C 8B DC                        mov r11, rsp
00C6F8DB  53                              push rbx
00C6F8DC  48 83 EC 40                     sub rsp, 0x40
00C6F8E0  4C 8B 0D 59 CB 31 00            mov r9, qword ptr [rip + 0x31cb59]
00C6F8E7  48 8D 05 9A 09 28 00            lea rax, [rip + 0x28099a]
00C6F8EE  49 83 63 08 00                  and qword ptr [r11 + 8], 0
00C6F8F3  4C 8D 05 CE 32 3D FF            lea r8, [rip - 0xc2cd32]
00C6F8FA  83 25 83 09 28 00 00            and dword ptr [rip + 0x280983], 0
00C6F901  BA 01 00 00 00                  mov edx, 1
00C6F906  48 89 05 83 09 28 00            mov qword ptr [rip + 0x280983], rax
00C6F90D  48 89 05 74 09 28 00            mov qword ptr [rip + 0x280974], rax
00C6F914  49 8D 43 08                     lea rax, [r11 + 8]
00C6F918  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
00C6F91C  48 8D 05 FD CB BC FF            lea rax, [rip - 0x433403]
00C6F923  49 83 63 E0 00                  and qword ptr [r11 - 0x20], 0
00C6F928  8D 4A 01                        lea ecx, [rdx + 1]
00C6F92B  49 89 43 D8                     mov qword ptr [r11 - 0x28], rax
00C6F92F  66 C7 05 48 09 28 00 01 00      mov word ptr [rip + 0x280948], 1
00C6F938  C6 05 43 09 28 00 06            mov byte ptr [rip + 0x280943], 6
00C6F93F  E8 5C 3C CE FF                  call 0x1409535a0
00C6F944  8B D8                           mov ebx, eax
00C6F946  85 C0                           test eax, eax
00C6F948  78 33                           js 0x140c6f97d
00C6F94A  48 8D 44 24 58                  lea rax, [rsp + 0x58]
00C6F94F  48 C7 44 24 58 00 1F 0A FA      mov qword ptr [rsp + 0x58], 0xfffffffffa0a1f00
00C6F958  45 33 C9                        xor r9d, r9d
00C6F95B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C6F960  45 33 C0                        xor r8d, r8d
00C6F963  48 8D 0D 16 09 28 00            lea rcx, [rip + 0x280916]
00C6F96A  33 D2                           xor edx, edx
00C6F96C  E8 3F ED 59 FF                  call 0x14020e6b0
00C6F971  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00C6F976  8B D8                           mov ebx, eax
00C6F978  E8 43 63 E3 FF                  call 0x140aa5cc0
00C6F97D  8B C3                           mov eax, ebx
00C6F97F  48 83 C4 40                     add rsp, 0x40
00C6F983  5B                              pop rbx
00C6F984  C3                              ret
00C6F985  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SbpWaitForVmbus(void)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (64);
    *(unsigned __int64 *)(v_rip + 2623875) = v_rip + 2623898;
    *(unsigned __int64 *)(v_rip + 2623860) = v_rip + 2623898;
    *(unsigned __int64 *)(v_rsp - 24) = v_rsp + 8;
    *(unsigned __int64 *)(v_rsp - 40) = v_rip - 4404227;
    *(unsigned __int16 *)(v_rip + 2623816) = 1;
    *(unsigned __int8 *)(v_rip + 2623811) = 6;
    result = IoRegisterPlugPlayNotification(1 + 1, 1, v_rip - 12766514, *(unsigned __int64 *)(v_rip + 3263321));
    v_rbx = (unsigned int)((unsigned int)(result));
    if (!(sign_flag)) {
        result = v_stack_p10;
        v_stack_p10 = 0xFFFFFFFFFA0A1F00ULL;
        a4 = 0;
        v_stack_m28 = result;
        a3 = 0;
        a1 = v_rip + 2623766;
        a2 = 0;
        result = KeWaitForSingleObject(a1, a2, a3, a4);
        a1 = v_stack_p8;
        v_rbx = (unsigned int)(result);
        result = IoUnregisterPlugPlayNotification(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return (unsigned int)((unsigned int)(v_rbx));
}
```

## 5. (Beta) C Style

```c
void SbpWaitForVmbus(void)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (64);
    *(uint64_t *)(v_rip + 0x280983) = v_rip + 2623898;
    *(uint64_t *)(v_rip + 0x280974) = v_rip + 2623898;
    *(uint64_t *)(local_rsp - 0x18) = local_rsp + 8;
    *(uint64_t *)(local_rsp - 0x28) = v_rip - 4404227;
    *(uint16_t *)(v_rip + 0x280948) = 1;
    *(uint8_t *)(v_rip + 0x280943) = 6;
    result = IoRegisterPlugPlayNotification(1 + 1, 1, v_rip - 12766514, *(uint64_t *)(v_rip + 0x31CB59));
    local_rbx = (uint32_t)((uint32_t)(result));
    if (!(sign_flag)) {
        result = v_stack_p10;
        v_stack_p10 = 0xFFFFFFFFFA0A1F00ULL;
        a4 = 0;
        v_stack_m28 = result;
        a3 = 0;
        a1 = v_rip + 2623766;
        a2 = 0;
        result = KeWaitForSingleObject(a1, a2, a3, a4);
        a1 = v_stack_p8;
        local_rbx = (uint32_t)(result);
        result = IoUnregisterPlugPlayNotification(a1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return (uint32_t)((uint32_t)(local_rbx));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C6F8D8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C6F8D8[BB_00C6F8D8]
  bb_00C6F94A[BB_00C6F94A]
  bb_00C6F97D[BB_00C6F97D]
  bb_00C6F985[BB_00C6F985]
  bb_00C6F8D8 -->|branch| bb_00C6F97D
  bb_00C6F8D8 -->|fallthrough| bb_00C6F94A
  bb_00C6F94A -->|flow| bb_00C6F97D
```
