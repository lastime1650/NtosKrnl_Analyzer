# sub_006FA5DC

- RVA: `0x006FA5DC`–`0x006FA5FB` (길이 `31` bytes)
- VA: `0x00000001406FA5DC`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B806C`
- 디코드: `7`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006FA5F0` → [RtlSetSystemGlobalData](../43/RtlSetSystemGlobalData_function_00435AF0.md) (function, `0x00435AF0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006FA5F6` → [HalpTimerPropagateQpcBiasUpdate + 0x25](../4A/HalpTimerPropagateQpcBiasUpdate_function_004AB9F4.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006FA5DC  41 B8 08 00 00 00               mov r8d, 8
006FA5E2  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
006FA5E7  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
006FA5EC  41 8D 48 0A                     lea ecx, [r8 + 0xa]
006FA5F0  E8 FB B4 D3 FF                  call 0x140435af0
006FA5F5  90                              nop
006FA5F6  E9 1E 14 DB FF                  jmp 0x1404aba19
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006FA5DC(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6)
{
    __int64 result;
    unsigned __int64 v_stack_p30;

    v_stack_p30 = result;
    result = RtlSetSystemGlobalData(8 + 10, a6, 8, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_006FA5DC(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, int64_t Arg6)
{
    int64_t result;
    uint64_t v_stack_p30;

    v_stack_p30 = result;
    result = RtlSetSystemGlobalData(8 + 10, Arg6, 8, Arg4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006FA5DC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006FA5DC[BB_006FA5DC]
```
