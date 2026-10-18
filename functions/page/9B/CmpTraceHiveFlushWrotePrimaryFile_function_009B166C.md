# CmpTraceHiveFlushWrotePrimaryFile

- RVA: `0x009B166C`–`0x009B1702` (길이 `150` bytes)
- VA: `0x00000001409B166C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009E2B4`
- 디코드: `39`개 명령, `150/150` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x009B16A1` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x009B16B1` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x009B16FB` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)

### Direct callers
- [HvWriteHivePrimaryFile](HvWriteHivePrimaryFile_function_009B2374.md) at `0x009B2504`

### Static image references
- `0x009B167C` → RVA `0x00E0A740` (`.data`; read)
- `0x009B168A` → RVA `0x00013C10` (`.rdata`; read)
- `0x009B1691` → RVA `0x00FD8018` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x009B16A1` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x009B16B1` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x009B16FB` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009B166C  89 54 24 10                     mov dword ptr [rsp + 0x10], edx
009B1670  89 4C 24 08                     mov dword ptr [rsp + 8], ecx
009B1674  55                              push rbp
009B1675  48 8B EC                        mov rbp, rsp
009B1678  48 83 EC 70                     sub rsp, 0x70
009B167C  48 8B 05 BD 90 45 00            mov rax, qword ptr [rip + 0x4590bd]
009B1683  48 33 C4                        xor rax, rsp
009B1686  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
009B168A  0F 10 05 7F 25 66 FF            movups xmm0, xmmword ptr [rip - 0x99da81]
009B1691  48 8B 0D 80 69 62 00            mov rcx, qword ptr [rip + 0x626980]
009B1698  48 8D 55 C0                     lea rdx, [rbp - 0x40]
009B169C  F3 0F 7F 45 C0                  movdqu xmmword ptr [rbp - 0x40], xmm0
009B16A1  E8 AA 0D 9E FF                  call 0x140392450
009B16A6  84 C0                           test al, al
009B16A8  75 13                           jne 0x1409b16bd
009B16AA  48 8B 4D F0                     mov rcx, qword ptr [rbp - 0x10]
009B16AE  48 33 CC                        xor rcx, rsp
009B16B1  E8 8A AF CF FF                  call 0x1406ac640
009B16B6  48 83 C4 70                     add rsp, 0x70
009B16BA  5D                              pop rbp
009B16BB  C3                              ret
009B16BC  CC                              int3
009B16BD  83 65 DC 00                     and dword ptr [rbp - 0x24], 0
009B16C1  48 8D 45 10                     lea rax, [rbp + 0x10]
009B16C5  83 65 EC 00                     and dword ptr [rbp - 0x14], 0
009B16C9  48 8D 55 C0                     lea rdx, [rbp - 0x40]
009B16CD  B9 04 00 00 00                  mov ecx, 4
009B16D2  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
009B16D6  48 8D 45 18                     lea rax, [rbp + 0x18]
009B16DA  89 4D D8                        mov dword ptr [rbp - 0x28], ecx
009B16DD  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
009B16E1  45 33 C0                        xor r8d, r8d
009B16E4  48 8D 45 D0                     lea rax, [rbp - 0x30]
009B16E8  89 4D E8                        mov dword ptr [rbp - 0x18], ecx
009B16EB  44 8D 49 FE                     lea r9d, [rcx - 2]
009B16EF  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009B16F4  48 8B 0D 1D 69 62 00            mov rcx, qword ptr [rip + 0x62691d]
009B16FB  E8 20 B0 A6 FF                  call 0x14041c720
009B1700  EB A8                           jmp 0x1409b16aa
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpTraceHiveFlushWrotePrimaryFile(int a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m2C;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p8;

    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (112);
    result = (*(unsigned __int64 *)(v_rip + 4559037)) ^ (v_rsp);
    v_stack_m18 = result;
    v_stack_m48 = v_xmm0;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 6449536), v_stack_m48, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_009B16BD;
loc_009B16AA:
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m48, a3, a4);
    v_rsp = (v_rsp) + (112);
    return result;
loc_009B16BD:
    v_stack_m38 = v_stack_p8;
    v_stack_m30 = 4;
    v_stack_m28 = v_stack_p10;
    a3 = 0;
    v_stack_m20 = 4;
    v_stack_p20 = v_stack_m38;
    result = EtwWrite(*(unsigned __int64 *)(v_rip + 6449437), v_stack_m48, a3, 4 - 2);
    goto loc_009B16AA;
}
```

## 5. (Beta) C Style

```c
int64_t CmpTraceHiveFlushWrotePrimaryFile(int32_t Arg1, int32_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint32_t v_stack_m2C;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m48;
    uint32_t v_stack_p10;
    uint64_t v_stack_p20;
    uint32_t v_stack_p8;

    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (112);
    result = (*(uint64_t *)(v_rip + 0x4590BD)) ^ (local_rsp);
    v_stack_m18 = result;
    v_stack_m48 = v_xmm0;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x626980), v_stack_m48, Arg3, a4);
    if ((uint8_t)(result) != 0) goto loc_009B16BD;
loc_009B16AA:
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m48, Arg3, a4);
    local_rsp = (local_rsp) + (112);
    return result;
loc_009B16BD:
    v_stack_m38 = v_stack_p8;
    v_stack_m30 = 4;
    v_stack_m28 = v_stack_p10;
    Arg3 = 0;
    v_stack_m20 = 4;
    v_stack_p20 = v_stack_m38;
    result = EtwWrite(*(uint64_t *)(v_rip + 0x62691D), v_stack_m48, Arg3, 4 - 2);
    goto loc_009B16AA;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009B166C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009B166C[BB_009B166C]
  bb_009B16AA[BB_009B16AA]
  bb_009B16BC[BB_009B16BC]
  bb_009B16BD[BB_009B16BD]
  bb_009B166C -->|branch| bb_009B16BD
  bb_009B166C -->|fallthrough| bb_009B16AA
  bb_009B16BC -->|flow| bb_009B16BD
  bb_009B16BD -->|branch| bb_009B16AA
```
