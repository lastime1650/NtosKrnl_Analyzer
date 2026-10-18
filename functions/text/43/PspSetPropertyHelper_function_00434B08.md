# PspSetPropertyHelper

- RVA: `0x00434B08`–`0x00434B23` (길이 `27` bytes)
- VA: `0x0000000140434B08`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CEE8`
- 디코드: `9`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00434B11` → [PspInsertProperty](PspInsertProperty_function_00434B2C.md) (function, `0x00434B2C`)
- `0x00434B1C` → [PspRemoveProperty](PspRemoveProperty_function_00434C10.md) (function, `0x00434C10`)

### Direct callers
- [PsSetThreadProperty](PsSetThreadProperty_function_00434A40.md) at `0x00434A60`
- [PsSetJobProperty](../5E/PsSetJobProperty_function_005E2E60.md) at `0x005E2EAB`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00434B08  48 83 EC 28                     sub rsp, 0x28
00434B0C  4D 85 C0                        test r8, r8
00434B0F  74 0B                           je 0x140434b1c
00434B11  E8 16 00 00 00                  call 0x140434b2c
00434B16  48 83 C4 28                     add rsp, 0x28
00434B1A  C3                              ret
00434B1B  CC                              int3
00434B1C  E8 EF 00 00 00                  call 0x140434c10
00434B21  EB F3                           jmp 0x140434b16
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspSetPropertyHelper(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a3 == 0) goto loc_00434B1C;
    result = PspInsertProperty(a1, a2, a3, a4);
loc_00434B16:
    v_rsp = (v_rsp) + (40);
    return result;
loc_00434B1C:
    result = PspRemoveProperty(a1, a2, a3, a4);
    goto loc_00434B16;
}
```

## 5. (Beta) C Style

```c
int64_t PspSetPropertyHelper(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg3 == 0) goto loc_00434B1C;
    result = PspInsertProperty(Arg1, Arg2, Arg3, a4);
loc_00434B16:
    local_rsp = (local_rsp) + (40);
    return result;
loc_00434B1C:
    result = PspRemoveProperty(Arg1, Arg2, Arg3, a4);
    goto loc_00434B16;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00434B08&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00434B08[BB_00434B08]
  bb_00434B11[BB_00434B11]
  bb_00434B16[BB_00434B16]
  bb_00434B1B[BB_00434B1B]
  bb_00434B1C[BB_00434B1C]
  bb_00434B08 -->|branch| bb_00434B1C
  bb_00434B08 -->|fallthrough| bb_00434B11
  bb_00434B11 -->|flow| bb_00434B16
  bb_00434B1B -->|flow| bb_00434B1C
  bb_00434B1C -->|branch| bb_00434B16
```
