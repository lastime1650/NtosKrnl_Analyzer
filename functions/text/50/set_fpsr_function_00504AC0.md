# set_fpsr

- RVA: `0x00504AC0`–`0x00504AD0` (길이 `16` bytes)
- VA: `0x0000000140504AC0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `4`개 명령, `16/16` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [ctrlfp](ctrlfp_function_005049B0.md) at `0x005049F2`
- [ctrlfp](ctrlfp_function_005049B0.md) at `0x00504A07`
- [ctrlfp](ctrlfp_function_005049B0.md) at `0x00504A15`
- [set_statfp](set_statfp_function_00504A40.md) at `0x00504A55`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00504AC0  89 4C 24 08                     mov dword ptr [rsp + 8], ecx
00504AC4  0F AE 54 24 08                  ldmxcsr dword ptr [rsp + 8]
00504AC9  C3                              ret
00504ACA  66 0F 1F 44 00 00               nop word ptr [rax + rax]
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall set_fpsr(int a1)
{
    unsigned int v_stack_p8;

    v_stack_p8 = a1;
    return;
}
```

## 5. (Beta) C Style

```c
void set_fpsr(int32_t Arg1)
{
    uint32_t v_stack_p8;

    v_stack_p8 = Arg1;
    return;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00504AC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00504AC0[BB_00504AC0]
  bb_00504ACA[BB_00504ACA]
```
