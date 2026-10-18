# PpmEventParkingCountSelectionEx

- RVA: `0x004F4188`–`0x004F42E4` (길이 `348` bytes)
- VA: `0x00000001404F4188`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BAA0C`
- 디코드: `71`개 명령, `348/348` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x004F41D3` → [EtwEventEnabled](../39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x004F42C8` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)
- `0x004F42D4` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PpmParkCalculateUnparkCount](../41/PpmParkCalculateUnparkCount_function_00413750.md) at `0x004139E5`

### Static image references
- `0x004F41A9` → RVA `0x00E0A740` (`.data`; read)
- `0x004F41B9` → RVA `0x00E67A39` (`.data`; read)
- `0x004F41C5` → RVA `0x00F083E8` (`.data`; read)
- `0x004F41CC` → RVA `0x0001C760` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004F4188  48 8B C4                        mov rax, rsp
004F418B  66 44 89 48 20                  mov word ptr [rax + 0x20], r9w
004F4190  66 44 89 40 18                  mov word ptr [rax + 0x18], r8w
004F4195  66 89 50 10                     mov word ptr [rax + 0x10], dx
004F4199  88 48 08                        mov byte ptr [rax + 8], cl
004F419C  55                              push rbp
004F419D  53                              push rbx
004F419E  48 8D 68 E8                     lea rbp, [rax - 0x18]
004F41A2  48 81 EC 08 01 00 00            sub rsp, 0x108
004F41A9  48 8B 05 90 65 91 00            mov rax, qword ptr [rip + 0x916590]
004F41B0  48 33 C4                        xor rax, rsp
004F41B3  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
004F41B7  33 DB                           xor ebx, ebx
004F41B9  38 1D 7A 38 97 00               cmp byte ptr [rip + 0x97387a], bl
004F41BF  0F 84 08 01 00 00               je 0x1404f42cd
004F41C5  48 8B 0D 1C 42 A1 00            mov rcx, qword ptr [rip + 0xa1421c]
004F41CC  48 8D 15 8D 85 B2 FF            lea rdx, [rip - 0x4d7a73]
004F41D3  E8 78 E2 E9 FF                  call 0x140392450
004F41D8  84 C0                           test al, al
004F41DA  0F 84 ED 00 00 00               je 0x1404f42cd
004F41E0  48 8B 0D 01 42 A1 00            mov rcx, qword ptr [rip + 0xa14201]
004F41E7  48 8D 45 20                     lea rax, [rbp + 0x20]
004F41EB  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
004F41F0  48 8D 15 69 85 B2 FF            lea rdx, [rip - 0x4d7a97]
004F41F7  48 8D 45 28                     lea rax, [rbp + 0x28]
004F41FB  48 C7 44 24 48 01 00 00 00      mov qword ptr [rsp + 0x48], 1
004F4204  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
004F4209  45 33 C9                        xor r9d, r9d
004F420C  48 8D 45 30                     lea rax, [rbp + 0x30]
004F4210  48 C7 44 24 58 02 00 00 00      mov qword ptr [rsp + 0x58], 2
004F4219  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
004F421E  45 33 C0                        xor r8d, r8d
004F4221  48 8D 45 38                     lea rax, [rbp + 0x38]
004F4225  48 C7 44 24 68 02 00 00 00      mov qword ptr [rsp + 0x68], 2
004F422E  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
004F4233  48 8D 45 40                     lea rax, [rbp + 0x40]
004F4237  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
004F423B  48 8D 45 48                     lea rax, [rbp + 0x48]
004F423F  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
004F4243  48 8D 45 50                     lea rax, [rbp + 0x50]
004F4247  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
004F424B  48 8D 45 58                     lea rax, [rbp + 0x58]
004F424F  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
004F4253  48 8D 45 60                     lea rax, [rbp + 0x60]
004F4257  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
004F425B  48 8D 45 68                     lea rax, [rbp + 0x68]
004F425F  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
004F4263  48 8D 45 70                     lea rax, [rbp + 0x70]
004F4267  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
004F426B  48 8D 44 24 40                  lea rax, [rsp + 0x40]
004F4270  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
004F4275  C7 44 24 30 0B 00 00 00         mov dword ptr [rsp + 0x30], 0xb
004F427D  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
004F4282  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
004F4287  48 C7 44 24 78 02 00 00 00      mov qword ptr [rsp + 0x78], 2
004F4290  48 C7 45 88 02 00 00 00         mov qword ptr [rbp - 0x78], 2
004F4298  48 C7 45 98 04 00 00 00         mov qword ptr [rbp - 0x68], 4
004F42A0  48 C7 45 A8 01 00 00 00         mov qword ptr [rbp - 0x58], 1
004F42A8  48 C7 45 B8 01 00 00 00         mov qword ptr [rbp - 0x48], 1
004F42B0  48 C7 45 C8 04 00 00 00         mov qword ptr [rbp - 0x38], 4
004F42B8  48 C7 45 D8 04 00 00 00         mov qword ptr [rbp - 0x28], 4
004F42C0  48 C7 45 E8 04 00 00 00         mov qword ptr [rbp - 0x18], 4
004F42C8  E8 03 AE D6 FF                  call 0x14025f0d0
004F42CD  48 8B 4D F0                     mov rcx, qword ptr [rbp - 0x10]
004F42D1  48 33 CC                        xor rcx, rsp
004F42D4  E8 67 83 1B 00                  call 0x1406ac640
004F42D9  48 81 C4 08 01 00 00            add rsp, 0x108
004F42E0  5B                              pop rbx
004F42E1  5D                              pop rbp
004F42E2  C3                              ret
004F42E3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmEventParkingCountSelectionEx(unsigned __int8 a1, unsigned __int16 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned int v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;

    *(unsigned __int16 *)(v_rsp + 32) = (unsigned __int16)(a4);
    *(unsigned __int16 *)(v_rsp + 24) = (unsigned __int16)(a3);
    *(unsigned __int16 *)(v_rsp + 16) = a2;
    *(unsigned __int8 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (264);
    result = (*(unsigned __int64 *)(v_rip + 9528720)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 24 - 16) = result;
    v_rbx = 0;
    if ((*(unsigned __int8 *)(v_rip + 9910394)) == 0) goto loc_004F42CD;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 10568220), v_rip - 5077619, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        a1 = *(unsigned __int64 *)(v_rip + 10568193);
        result = v_rsp - 24 + 32;
        v_stack_mD8 = result;
        a2 = v_rip - 5077655;
        result = v_rsp - 24 + 40;
        v_stack_mD0 = 1;
        v_stack_mC8 = result;
        a4 = 0;
        result = v_rsp - 24 + 48;
        v_stack_mC0 = 2;
        v_stack_mB8 = result;
        a3 = 0;
        result = v_rsp - 24 + 56;
        v_stack_mB0 = 2;
        v_stack_mA8 = result;
        result = v_rsp - 24 + 64;
        *(unsigned __int64 *)(v_rsp - 24 - 128) = result;
        result = v_rsp - 24 + 72;
        *(unsigned __int64 *)(v_rsp - 24 - 112) = result;
        result = v_rsp - 24 + 80;
        *(unsigned __int64 *)(v_rsp - 24 - 96) = result;
        result = v_rsp - 24 + 88;
        *(unsigned __int64 *)(v_rsp - 24 - 80) = result;
        result = v_rsp - 24 + 96;
        *(unsigned __int64 *)(v_rsp - 24 - 64) = result;
        result = v_rsp - 24 + 104;
        *(unsigned __int64 *)(v_rsp - 24 - 48) = result;
        result = v_rsp - 24 + 112;
        *(unsigned __int64 *)(v_rsp - 24 - 32) = result;
        result = v_stack_mD8;
        v_stack_mE0 = result;
        v_stack_mE8 = 11;
        v_stack_mF0 = 0;
        v_stack_mF8 = 0;
        v_stack_mA0 = 2;
        *(unsigned __int64 *)(v_rsp - 24 - 120) = 2;
        *(unsigned __int64 *)(v_rsp - 24 - 104) = 4;
        *(unsigned __int64 *)(v_rsp - 24 - 88) = 1;
        *(unsigned __int64 *)(v_rsp - 24 - 72) = 1;
        *(unsigned __int64 *)(v_rsp - 24 - 56) = 4;
        *(unsigned __int64 *)(v_rsp - 24 - 40) = 4;
        *(unsigned __int64 *)(v_rsp - 24 - 24) = 4;
        result = EtwWriteEx(a1, a2, a3, a4);
    }
    a1 = (*(unsigned __int64 *)(v_rsp - 24 - 16)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (264);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PpmEventParkingCountSelectionEx(uint8_t Arg1, uint16_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint32_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;

    *(uint16_t *)(local_rsp + 0x20) = (uint16_t)(Arg4);
    *(uint16_t *)(local_rsp + 0x18) = (uint16_t)(Arg3);
    *(uint16_t *)(local_rsp + 0x10) = Arg2;
    *(uint8_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (264);
    result = (*(uint64_t *)(v_rip + 0x916590)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x18 - 0x10) = result;
    local_rbx = 0;
    if ((*(uint8_t *)(v_rip + 0x97387A)) == 0) goto loc_004F42CD;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0xA1421C), v_rip - 5077619, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        Arg1 = *(uint64_t *)(v_rip + 0xA14201);
        result = local_rsp - 24 + 32;
        v_stack_mD8 = result;
        Arg2 = v_rip - 5077655;
        result = local_rsp - 24 + 40;
        v_stack_mD0 = 1;
        v_stack_mC8 = result;
        Arg4 = 0;
        result = local_rsp - 24 + 48;
        v_stack_mC0 = 2;
        v_stack_mB8 = result;
        Arg3 = 0;
        result = local_rsp - 24 + 56;
        v_stack_mB0 = 2;
        v_stack_mA8 = result;
        result = local_rsp - 24 + 64;
        *(uint64_t *)(local_rsp - 0x18 - 0x80) = result;
        result = local_rsp - 24 + 72;
        *(uint64_t *)(local_rsp - 0x18 - 0x70) = result;
        result = local_rsp - 24 + 80;
        *(uint64_t *)(local_rsp - 0x18 - 0x60) = result;
        result = local_rsp - 24 + 88;
        *(uint64_t *)(local_rsp - 0x18 - 0x50) = result;
        result = local_rsp - 24 + 96;
        *(uint64_t *)(local_rsp - 0x18 - 0x40) = result;
        result = local_rsp - 24 + 104;
        *(uint64_t *)(local_rsp - 0x18 - 0x30) = result;
        result = local_rsp - 24 + 112;
        *(uint64_t *)(local_rsp - 0x18 - 0x20) = result;
        result = v_stack_mD8;
        v_stack_mE0 = result;
        v_stack_mE8 = 11;
        v_stack_mF0 = 0;
        v_stack_mF8 = 0;
        v_stack_mA0 = 2;
        *(uint64_t *)(local_rsp - 0x18 - 0x78) = 2;
        *(uint64_t *)(local_rsp - 0x18 - 0x68) = 4;
        *(uint64_t *)(local_rsp - 0x18 - 0x58) = 1;
        *(uint64_t *)(local_rsp - 0x18 - 0x48) = 1;
        *(uint64_t *)(local_rsp - 0x18 - 0x38) = 4;
        *(uint64_t *)(local_rsp - 0x18 - 0x28) = 4;
        *(uint64_t *)(local_rsp - 0x18 - 0x18) = 4;
        result = EtwWriteEx(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (*(uint64_t *)(local_rsp - 0x18 - 0x10)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (264);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004F4188&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004F4188[BB_004F4188]
  bb_004F41C5[BB_004F41C5]
  bb_004F41E0[BB_004F41E0]
  bb_004F42CD[BB_004F42CD]
  bb_004F42E3[BB_004F42E3]
  bb_004F4188 -->|branch| bb_004F42CD
  bb_004F4188 -->|fallthrough| bb_004F41C5
  bb_004F41C5 -->|branch| bb_004F42CD
  bb_004F41C5 -->|fallthrough| bb_004F41E0
  bb_004F41E0 -->|flow| bb_004F42CD
```
