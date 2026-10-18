# PpmEventHeteroFavoredCoreRotationChange

- RVA: `0x0047ACB0`–`0x0047AD66` (길이 `182` bytes)
- VA: `0x000000014047ACB0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AD3B0`
- 디코드: `38`개 명령, `182/182` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x0047ACE2` → [EtwEventEnabled](../39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x0047AD4E` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)
- `0x0047AD5B` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PpmParkComputeUnparkMaskEx](../5E/PpmParkComputeUnparkMaskEx_function_005E05E0.md) at `0x005E0E00`
- [sub_006F3648](../6F/Unknown_function_006F3648.md) at `0x006F3933`

### Static image references
- `0x0047ACBC` → RVA `0x00E0A740` (`.data`; read)
- `0x0047ACCB` → RVA `0x00E67A39` (`.data`; read)
- `0x0047ACD4` → RVA `0x00F083E8` (`.data`; read)
- `0x0047ACDB` → RVA `0x0001A2F0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0047ACB0  89 54 24 10                     mov dword ptr [rsp + 0x10], edx
0047ACB4  89 4C 24 08                     mov dword ptr [rsp + 8], ecx
0047ACB8  48 83 EC 78                     sub rsp, 0x78
0047ACBC  48 8B 05 7D FA 98 00            mov rax, qword ptr [rip + 0x98fa7d]
0047ACC3  48 33 C4                        xor rax, rsp
0047ACC6  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
0047ACCB  80 3D 67 CD 9E 00 00            cmp byte ptr [rip + 0x9ecd67], 0
0047ACD2  74 7F                           je 0x14047ad53
0047ACD4  48 8B 0D 0D D7 A8 00            mov rcx, qword ptr [rip + 0xa8d70d]
0047ACDB  48 8D 15 0E F6 B9 FF            lea rdx, [rip - 0x4609f2]
0047ACE2  E8 69 77 F1 FF                  call 0x140392450
0047ACE7  84 C0                           test al, al
0047ACE9  74 68                           je 0x14047ad53
0047ACEB  83 64 24 4C 00                  and dword ptr [rsp + 0x4c], 0
0047ACF0  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
0047ACF8  83 64 24 5C 00                  and dword ptr [rsp + 0x5c], 0
0047ACFD  48 8D 15 EC F5 B9 FF            lea rdx, [rip - 0x460a14]
0047AD04  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0047AD09  B9 04 00 00 00                  mov ecx, 4
0047AD0E  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
0047AD16  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
0047AD1A  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0047AD1F  45 33 C9                        xor r9d, r9d
0047AD22  48 8D 44 24 40                  lea rax, [rsp + 0x40]
0047AD27  89 4C 24 58                     mov dword ptr [rsp + 0x58], ecx
0047AD2B  48 8B 0D B6 D6 A8 00            mov rcx, qword ptr [rip + 0xa8d6b6]
0047AD32  45 33 C0                        xor r8d, r8d
0047AD35  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0047AD3A  C7 44 24 30 02 00 00 00         mov dword ptr [rsp + 0x30], 2
0047AD42  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
0047AD48  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
0047AD4E  E8 7D 43 DE FF                  call 0x14025f0d0
0047AD53  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
0047AD58  48 33 CC                        xor rcx, rsp
0047AD5B  E8 E0 18 23 00                  call 0x1406ac640
0047AD60  48 83 C4 78                     add rsp, 0x78
0047AD64  C3                              ret
0047AD65  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmEventHeteroFavoredCoreRotationChange(int a1, int a2, int a3, int a4)
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
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_p10;
    unsigned int v_stack_p8;

    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (120);
    result = (*(unsigned __int64 *)(v_rip + 10025597)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((*(unsigned __int8 *)(v_rip + 10407271)) == 0) goto loc_0047AD53;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 11065101), v_rip - 4590066, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_p8;
        a2 = v_rip - 4590100;
        v_stack_m38 = result;
        a1 = 4;
        result = v_stack_p10;
        v_stack_m30 = a1;
        v_stack_m28 = result;
        a4 = 0;
        result = v_stack_m38;
        v_stack_m20 = a1;
        a1 = *(unsigned __int64 *)(v_rip + 11065014);
        a3 = 0;
        v_stack_m40 = result;
        v_stack_m48 = 2;
        result = EtwWriteEx(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (120);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PpmEventHeteroFavoredCoreRotationChange(int32_t Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4)
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
    uint64_t v_stack_m40;
    uint32_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_p10;
    uint32_t v_stack_p8;

    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (120);
    result = (*(uint64_t *)(v_rip + 0x98FA7D)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((*(uint8_t *)(v_rip + 0x9ECD67)) == 0) goto loc_0047AD53;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0xA8D70D), v_rip - 4590066, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = v_stack_p8;
        Arg2 = v_rip - 4590100;
        v_stack_m38 = result;
        Arg1 = 4;
        result = v_stack_p10;
        v_stack_m30 = Arg1;
        v_stack_m28 = result;
        Arg4 = 0;
        result = v_stack_m38;
        v_stack_m20 = Arg1;
        Arg1 = *(uint64_t *)(v_rip + 0xA8D6B6);
        Arg3 = 0;
        v_stack_m40 = result;
        v_stack_m48 = 2;
        result = EtwWriteEx(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (120);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0047ACB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0047ACB0[BB_0047ACB0]
  bb_0047ACD4[BB_0047ACD4]
  bb_0047ACEB[BB_0047ACEB]
  bb_0047AD53[BB_0047AD53]
  bb_0047AD65[BB_0047AD65]
  bb_0047ACB0 -->|branch| bb_0047AD53
  bb_0047ACB0 -->|fallthrough| bb_0047ACD4
  bb_0047ACD4 -->|branch| bb_0047AD53
  bb_0047ACD4 -->|fallthrough| bb_0047ACEB
  bb_0047ACEB -->|flow| bb_0047AD53
```
