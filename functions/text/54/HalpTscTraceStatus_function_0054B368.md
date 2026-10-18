# HalpTscTraceStatus

- RVA: `0x0054B368`–`0x0054B3FD` (길이 `149` bytes)
- VA: `0x000000014054B368`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AD30C`
- 디코드: `35`개 명령, `149/149` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0054B396` → [EtwEventEnabled](../39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x0054B3E4` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)
- `0x0054B3F1` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [HalpTscAdvSynchLeader](HalpTscAdvSynchLeader_function_0054A690.md) at `0x0054A825`
- [HalpTscFallbackToPlatformSource](HalpTscFallbackToPlatformSource_function_0054AD14.md) at `0x0054AD8C`

### Static image references
- `0x0054B371` → RVA `0x00E0A740` (`.data`; read)
- `0x0054B380` → RVA `0x00FC22C0` (`.data`; read)
- `0x0054B38F` → RVA `0x00FC22B8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0054B368  89 54 24 10                     mov dword ptr [rsp + 0x10], edx
0054B36C  53                              push rbx
0054B36D  48 83 EC 60                     sub rsp, 0x60
0054B371  48 8B 05 C8 F3 8B 00            mov rax, qword ptr [rip + 0x8bf3c8]
0054B378  48 33 C4                        xor rax, rsp
0054B37B  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0054B380  80 3D 39 6F A7 00 00            cmp byte ptr [rip + 0xa76f39], 0
0054B387  48 8B D9                        mov rbx, rcx
0054B38A  74 5D                           je 0x14054b3e9
0054B38C  48 8B D1                        mov rdx, rcx
0054B38F  48 8B 0D 22 6F A7 00            mov rcx, qword ptr [rip + 0xa76f22]
0054B396  E8 B5 70 E4 FF                  call 0x140392450
0054B39B  84 C0                           test al, al
0054B39D  74 4A                           je 0x14054b3e9
0054B39F  83 64 24 4C 00                  and dword ptr [rsp + 0x4c], 0
0054B3A4  48 8D 44 24 78                  lea rax, [rsp + 0x78]
0054B3A9  48 8B 0D 08 6F A7 00            mov rcx, qword ptr [rip + 0xa76f08]
0054B3B0  45 33 C9                        xor r9d, r9d
0054B3B3  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0054B3B8  45 33 C0                        xor r8d, r8d
0054B3BB  48 8D 44 24 40                  lea rax, [rsp + 0x40]
0054B3C0  C7 44 24 48 04 00 00 00         mov dword ptr [rsp + 0x48], 4
0054B3C8  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0054B3CD  48 8B D3                        mov rdx, rbx
0054B3D0  C7 44 24 30 01 00 00 00         mov dword ptr [rsp + 0x30], 1
0054B3D8  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
0054B3DE  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
0054B3E4  E8 E7 3C D1 FF                  call 0x14025f0d0
0054B3E9  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
0054B3EE  48 33 CC                        xor rcx, rsp
0054B3F1  E8 4A 12 16 00                  call 0x1406ac640
0054B3F6  48 83 C4 60                     add rsp, 0x60
0054B3FA  5B                              pop rbx
0054B3FB  C3                              ret
0054B3FC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpTscTraceStatus(__int64 a1, int a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned int v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_p10;

    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (96);
    result = (*(unsigned __int64 *)(v_rip + 9171912)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((*(unsigned __int8 *)(v_rip + 10972985)) == 0) goto loc_0054B3E9;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 10972962), a1, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_p10;
        a1 = *(unsigned __int64 *)(v_rip + 10972936);
        a4 = 0;
        v_stack_m28 = result;
        a3 = 0;
        result = v_stack_m28;
        v_stack_m20 = 4;
        v_stack_m30 = result;
        a2 = a1;
        v_stack_m38 = 1;
        result = EtwWriteEx(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (96);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalpTscTraceStatus(int64_t Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint32_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_p10;

    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (96);
    result = (*(uint64_t *)(v_rip + 0x8BF3C8)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((*(uint8_t *)(v_rip + 0xA76F39)) == 0) goto loc_0054B3E9;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0xA76F22), Arg1, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = v_stack_p10;
        Arg1 = *(uint64_t *)(v_rip + 0xA76F08);
        Arg4 = 0;
        v_stack_m28 = result;
        Arg3 = 0;
        result = v_stack_m28;
        v_stack_m20 = 4;
        v_stack_m30 = result;
        Arg2 = Arg1;
        v_stack_m38 = 1;
        result = EtwWriteEx(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (96);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0054B368&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0054B368[BB_0054B368]
  bb_0054B38C[BB_0054B38C]
  bb_0054B39F[BB_0054B39F]
  bb_0054B3E9[BB_0054B3E9]
  bb_0054B3FC[BB_0054B3FC]
  bb_0054B368 -->|branch| bb_0054B3E9
  bb_0054B368 -->|fallthrough| bb_0054B38C
  bb_0054B38C -->|branch| bb_0054B3E9
  bb_0054B38C -->|fallthrough| bb_0054B39F
  bb_0054B39F -->|flow| bb_0054B3E9
```
