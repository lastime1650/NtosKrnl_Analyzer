# PopTraceSmbiosChange

- RVA: `0x005D7D88`–`0x005D7E6D` (길이 `229` bytes)
- VA: `0x00000001405D7D88`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AC058`
- 디코드: `52`개 명령, `229/229` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x005D7DC8` → [tlgKeywordOn](../42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x005D7E52` → [tlgWriteTransfer_EtwWriteTransfer](../42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x005D7E5E` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopUpdateSmbiosData](../../page/76/PopUpdateSmbiosData_function_007602BC.md) at `0x00760302`

### Static image references
- `0x005D7D96` → RVA `0x00E0A740` (`.data`; read)
- `0x005D7DA4` → RVA `0x00E07748` (`.data`; read)
- `0x005D7E37` → RVA `0x0004B18A` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005D7D88  40 55                           push rbp
005D7D8A  48 8D 6C 24 A9                  lea rbp, [rsp - 0x57]
005D7D8F  48 81 EC C0 00 00 00            sub rsp, 0xc0
005D7D96  48 8B 05 A3 29 83 00            mov rax, qword ptr [rip + 0x8329a3]
005D7D9D  48 33 C4                        xor rax, rsp
005D7DA0  48 89 45 47                     mov qword ptr [rbp + 0x47], rax
005D7DA4  83 3D 9D F9 82 00 05            cmp dword ptr [rip + 0x82f99d], 5
005D7DAB  44 8B DA                        mov r11d, edx
005D7DAE  4C 8B D1                        mov r10, rcx
005D7DB1  0F 86 A0 00 00 00               jbe 0x1405d7e57
005D7DB7  48 BA 00 00 00 00 00 40 00 00   movabs rdx, 0x400000000000
005D7DC1  48 8D 0D 80 F9 82 00            lea rcx, [rip + 0x82f980]
005D7DC8  E8 D3 6C E5 FF                  call 0x14042eaa0
005D7DCD  84 C0                           test al, al
005D7DCF  0F 84 82 00 00 00               je 0x1405d7e57
005D7DD5  83 65 13 00                     and dword ptr [rbp + 0x13], 0
005D7DD9  48 8D 45 CF                     lea rax, [rbp - 0x31]
005D7DDD  83 65 23 00                     and dword ptr [rbp + 0x23], 0
005D7DE1  48 8D 0D 60 F9 82 00            lea rcx, [rip + 0x82f960]
005D7DE8  83 65 33 00                     and dword ptr [rbp + 0x33], 0
005D7DEC  83 65 43 00                     and dword ptr [rbp + 0x43], 0
005D7DF0  48 89 45 07                     mov qword ptr [rbp + 7], rax
005D7DF4  48 8D 45 C7                     lea rax, [rbp - 0x39]
005D7DF8  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
005D7DFC  48 8D 45 D7                     lea rax, [rbp - 0x29]
005D7E00  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
005D7E04  48 8D 45 CB                     lea rax, [rbp - 0x35]
005D7E08  4C 89 55 CF                     mov qword ptr [rbp - 0x31], r10
005D7E0C  41 BA 08 00 00 00               mov r10d, 8
005D7E12  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
005D7E16  48 8D 45 E7                     lea rax, [rbp - 0x19]
005D7E1A  4C 89 45 D7                     mov qword ptr [rbp - 0x29], r8
005D7E1E  45 33 C0                        xor r8d, r8d
005D7E21  44 89 4D CB                     mov dword ptr [rbp - 0x35], r9d
005D7E25  45 33 C9                        xor r9d, r9d
005D7E28  41 8D 52 FC                     lea edx, [r10 - 4]
005D7E2C  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
005D7E31  89 55 1F                        mov dword ptr [rbp + 0x1f], edx
005D7E34  89 55 3F                        mov dword ptr [rbp + 0x3f], edx
005D7E37  48 8D 15 4C 33 A7 FF            lea rdx, [rip - 0x58ccb4]
005D7E3E  C7 44 24 20 06 00 00 00         mov dword ptr [rsp + 0x20], 6
005D7E46  44 89 55 0F                     mov dword ptr [rbp + 0xf], r10d
005D7E4A  44 89 5D C7                     mov dword ptr [rbp - 0x39], r11d
005D7E4E  44 89 55 2F                     mov dword ptr [rbp + 0x2f], r10d
005D7E52  E8 89 E2 E4 FF                  call 0x1404260e0
005D7E57  48 8B 4D 47                     mov rcx, qword ptr [rbp + 0x47]
005D7E5B  48 33 CC                        xor rcx, rsp
005D7E5E  E8 DD 47 0D 00                  call 0x1406ac640
005D7E63  48 81 C4 C0 00 00 00            add rsp, 0xc0
005D7E6A  5D                              pop rbp
005D7E6B  C3                              ret
005D7E6C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopTraceSmbiosChange(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m2C;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m3C;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m4C;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m94;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned int v_stack_mA8;

    v_rsp = (v_rsp) - (192);
    result = (*(unsigned __int64 *)(v_rip + 8595875)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((*(unsigned int *)(v_rip + 8583581)) <= 5) goto loc_005D7E57;
    result = tlgKeywordOn(v_rip + 8583552, a2, a3, a4);
    v_r10 = a1;
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_m90;
        a1 = v_rip + 8583520;
        v_stack_m58 = result;
        result = v_stack_m98;
        v_stack_m48 = result;
        result = v_stack_m88;
        v_stack_m38 = result;
        result = v_stack_m94;
        v_stack_m90 = a1;
        v_r10 = 8;
        v_stack_m28 = result;
        result = v_stack_m78;
        v_stack_m88 = a3;
        a3 = 0;
        v_stack_m94 = a4;
        a4 = 0;
        a2 = v_r10 - 4;
        v_stack_mA0 = result;
        v_stack_m40 = a2;
        v_stack_m20 = a2;
        a2 = v_rip - 5819572;
        v_stack_mA8 = 6;
        v_stack_m50 = (unsigned int)(v_r10);
        v_stack_m98 = (unsigned int)((unsigned int)(a2));
        v_stack_m30 = (unsigned int)(v_r10);
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (192);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopTraceSmbiosChange(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint32_t v_stack_m2C;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint32_t v_stack_m3C;
    uint32_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_m4C;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m78;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m94;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint32_t v_stack_mA8;

    local_rsp = (local_rsp) - (192);
    result = (*(uint64_t *)(v_rip + 0x8329A3)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((*(uint32_t *)(v_rip + 0x82F99D)) <= 5) goto loc_005D7E57;
    result = tlgKeywordOn(v_rip + 8583552, Arg2, Arg3, Arg4);
    local_r10 = Arg1;
    if ((uint8_t)(result) != 0) {
        result = v_stack_m90;
        Arg1 = v_rip + 8583520;
        v_stack_m58 = result;
        result = v_stack_m98;
        v_stack_m48 = result;
        result = v_stack_m88;
        v_stack_m38 = result;
        result = v_stack_m94;
        v_stack_m90 = Arg1;
        local_r10 = 8;
        v_stack_m28 = result;
        result = v_stack_m78;
        v_stack_m88 = Arg3;
        Arg3 = 0;
        v_stack_m94 = Arg4;
        Arg4 = 0;
        Arg2 = local_r10 - 4;
        v_stack_mA0 = result;
        v_stack_m40 = Arg2;
        v_stack_m20 = Arg2;
        Arg2 = v_rip - 5819572;
        v_stack_mA8 = 6;
        v_stack_m50 = (uint32_t)(local_r10);
        v_stack_m98 = (uint32_t)((uint32_t)(Arg2));
        v_stack_m30 = (uint32_t)(local_r10);
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (192);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005D7D88&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005D7D88[BB_005D7D88]
  bb_005D7DB7[BB_005D7DB7]
  bb_005D7DD5[BB_005D7DD5]
  bb_005D7E57[BB_005D7E57]
  bb_005D7E6C[BB_005D7E6C]
  bb_005D7D88 -->|branch| bb_005D7E57
  bb_005D7D88 -->|fallthrough| bb_005D7DB7
  bb_005D7DB7 -->|branch| bb_005D7E57
  bb_005D7DB7 -->|fallthrough| bb_005D7DD5
  bb_005D7DD5 -->|flow| bb_005D7E57
```
