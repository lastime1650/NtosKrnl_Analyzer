# KdTrap

- RVA: `0x00431680`–`0x004316B1` (길이 `49` bytes)
- VA: `0x0000000140431680`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000789BC`
- 디코드: `13`개 명령, `49/49` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0043169F` → [KdpStub](KdpStub_function_004316C0.md) (function, `0x004316C0`)
- `0x004316AA` → [KdpTrap](../../pagekd/B8/KdpTrap_function_00B852B8.md) (function, `0x00B852B8`)

### Direct callers
- [KiDispatchException](../3D/KiDispatchException_function_003D7650.md) at `0x003D77E7`
- [KiDispatchException](../3D/KiDispatchException_function_003D7650.md) at `0x003D790E`
- [KiDispatchException](../3D/KiDispatchException_function_003D7650.md) at `0x003D79E0`

### Static image references
- `0x00431684` → RVA `0x00E664A8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x004316AA` → [KdpTrap](../../pagekd/B8/KdpTrap_function_00B852B8.md) (`.text` → `PAGEKD`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00431680  48 83 EC 38                     sub rsp, 0x38
00431684  83 3D 1D 4E A3 00 00            cmp dword ptr [rip + 0xa34e1d], 0
0043168B  0F B6 44 24 68                  movzx eax, byte ptr [rsp + 0x68]
00431690  88 44 24 28                     mov byte ptr [rsp + 0x28], al
00431694  0F B6 44 24 60                  movzx eax, byte ptr [rsp + 0x60]
00431699  88 44 24 20                     mov byte ptr [rsp + 0x20], al
0043169D  75 0B                           jne 0x1404316aa
0043169F  E8 1C 00 00 00                  call 0x1404316c0
004316A4  48 83 C4 38                     add rsp, 0x38
004316A8  C3                              ret
004316A9  CC                              int3
004316AA  E8 09 3C 75 00                  call 0x140b852b8
004316AF  EB F3                           jmp 0x1404316a4
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KdTrap(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned __int8 a5, unsigned __int8 a6)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int8 v_stack_m10;
    unsigned __int8 v_stack_m18;

    v_rsp = (v_rsp) - (56);
    v_stack_m10 = a6;
    v_stack_m18 = a5;
    if ((*(unsigned int *)(v_rip + 10702365)) != 0) goto loc_004316AA;
    result = KdpStub(a1, a2, a3, a4);
loc_004316A4:
    v_rsp = (v_rsp) + (56);
    return result;
loc_004316AA:
    result = KdpTrap(a1, a2, a3, a4);
    goto loc_004316A4;
}
```

## 5. (Beta) C Style

```c
int64_t KdTrap(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint8_t Arg5, uint8_t Arg6)
{
    int64_t result;
    int64_t local_rsp;
    uint8_t v_stack_m10;
    uint8_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    v_stack_m10 = Arg6;
    v_stack_m18 = Arg5;
    if ((*(uint32_t *)(v_rip + 0xA34E1D)) != 0) goto loc_004316AA;
    result = KdpStub(Arg1, Arg2, Arg3, Arg4);
loc_004316A4:
    local_rsp = (local_rsp) + (56);
    return result;
loc_004316AA:
    result = KdpTrap(Arg1, Arg2, Arg3, Arg4);
    goto loc_004316A4;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00431680&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00431680[BB_00431680]
  bb_0043169F[BB_0043169F]
  bb_004316A4[BB_004316A4]
  bb_004316A9[BB_004316A9]
  bb_004316AA[BB_004316AA]
  bb_00431680 -->|branch| bb_004316AA
  bb_00431680 -->|fallthrough| bb_0043169F
  bb_0043169F -->|flow| bb_004316A4
  bb_004316A9 -->|flow| bb_004316AA
  bb_004316AA -->|branch| bb_004316A4
```
