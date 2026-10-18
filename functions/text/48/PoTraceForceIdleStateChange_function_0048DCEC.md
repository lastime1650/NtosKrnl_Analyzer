# PoTraceForceIdleStateChange

- RVA: `0x0048DCEC`–`0x0048DDA2` (길이 `182` bytes)
- VA: `0x000000014048DCEC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AD3B0`
- 디코드: `38`개 명령, `182/182` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x0048DD1E` → [EtwEventEnabled](../39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x0048DD8A` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)
- `0x0048DD97` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [KiSetForceIdleState](KiSetForceIdleState_function_0048DCC0.md) at `0x0048DCD6`

### Static image references
- `0x0048DCF8` → RVA `0x00E0A740` (`.data`; read)
- `0x0048DD07` → RVA `0x00E67858` (`.data`; read)
- `0x0048DD10` → RVA `0x00F0B408` (`.data`; read)
- `0x0048DD17` → RVA `0x0001A728` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0048DCEC  89 54 24 10                     mov dword ptr [rsp + 0x10], edx
0048DCF0  89 4C 24 08                     mov dword ptr [rsp + 8], ecx
0048DCF4  48 83 EC 78                     sub rsp, 0x78
0048DCF8  48 8B 05 41 CA 97 00            mov rax, qword ptr [rip + 0x97ca41]
0048DCFF  48 33 C4                        xor rax, rsp
0048DD02  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
0048DD07  80 3D 4A 9B 9D 00 00            cmp byte ptr [rip + 0x9d9b4a], 0
0048DD0E  74 7F                           je 0x14048dd8f
0048DD10  48 8B 0D F1 D6 A7 00            mov rcx, qword ptr [rip + 0xa7d6f1]
0048DD17  48 8D 15 0A CA B8 FF            lea rdx, [rip - 0x4735f6]
0048DD1E  E8 2D 47 F0 FF                  call 0x140392450
0048DD23  84 C0                           test al, al
0048DD25  74 68                           je 0x14048dd8f
0048DD27  83 64 24 4C 00                  and dword ptr [rsp + 0x4c], 0
0048DD2C  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
0048DD34  83 64 24 5C 00                  and dword ptr [rsp + 0x5c], 0
0048DD39  48 8D 15 E8 C9 B8 FF            lea rdx, [rip - 0x473618]
0048DD40  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0048DD45  B9 04 00 00 00                  mov ecx, 4
0048DD4A  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
0048DD52  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
0048DD56  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0048DD5B  45 33 C9                        xor r9d, r9d
0048DD5E  48 8D 44 24 40                  lea rax, [rsp + 0x40]
0048DD63  89 4C 24 58                     mov dword ptr [rsp + 0x58], ecx
0048DD67  48 8B 0D 9A D6 A7 00            mov rcx, qword ptr [rip + 0xa7d69a]
0048DD6E  45 33 C0                        xor r8d, r8d
0048DD71  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0048DD76  C7 44 24 30 02 00 00 00         mov dword ptr [rsp + 0x30], 2
0048DD7E  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
0048DD84  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
0048DD8A  E8 41 13 DD FF                  call 0x14025f0d0
0048DD8F  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
0048DD94  48 33 CC                        xor rcx, rsp
0048DD97  E8 A4 E8 21 00                  call 0x1406ac640
0048DD9C  48 83 C4 78                     add rsp, 0x78
0048DDA0  C3                              ret
0048DDA1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PoTraceForceIdleStateChange(int a1, int a2, int a3, int a4)
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
    result = (*(unsigned __int64 *)(v_rip + 9947713)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((*(unsigned __int8 *)(v_rip + 10328906)) == 0) goto loc_0048DD8F;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 10999537), v_rip - 4666870, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_p8;
        a2 = v_rip - 4666904;
        v_stack_m38 = result;
        a1 = 4;
        result = v_stack_p10;
        v_stack_m30 = a1;
        v_stack_m28 = result;
        a4 = 0;
        result = v_stack_m38;
        v_stack_m20 = a1;
        a1 = *(unsigned __int64 *)(v_rip + 10999450);
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
int64_t PoTraceForceIdleStateChange(int32_t Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4)
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
    result = (*(uint64_t *)(v_rip + 0x97CA41)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((*(uint8_t *)(v_rip + 0x9D9B4A)) == 0) goto loc_0048DD8F;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0xA7D6F1), v_rip - 4666870, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = v_stack_p8;
        Arg2 = v_rip - 4666904;
        v_stack_m38 = result;
        Arg1 = 4;
        result = v_stack_p10;
        v_stack_m30 = Arg1;
        v_stack_m28 = result;
        Arg4 = 0;
        result = v_stack_m38;
        v_stack_m20 = Arg1;
        Arg1 = *(uint64_t *)(v_rip + 0xA7D69A);
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

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0048DCEC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0048DCEC[BB_0048DCEC]
  bb_0048DD10[BB_0048DD10]
  bb_0048DD27[BB_0048DD27]
  bb_0048DD8F[BB_0048DD8F]
  bb_0048DDA1[BB_0048DDA1]
  bb_0048DCEC -->|branch| bb_0048DD8F
  bb_0048DCEC -->|fallthrough| bb_0048DD10
  bb_0048DD10 -->|branch| bb_0048DD8F
  bb_0048DD10 -->|fallthrough| bb_0048DD27
  bb_0048DD27 -->|flow| bb_0048DD8F
```
