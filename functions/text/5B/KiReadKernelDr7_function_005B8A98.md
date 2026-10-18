# KiReadKernelDr7

- RVA: `0x005B8A98`–`0x005B8ABB` (길이 `35` bytes)
- VA: `0x00000001405B8A98`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `9`개 명령, `35/35` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [KiSwInterruptDispatch](../50/KiSwInterruptDispatch_function_0050A5C0.md) at `0x0050BBF3`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005B8A98  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
005B8AA1  48 8B 88 48 01 00 00            mov rcx, qword ptr [rax + 0x148]
005B8AA8  48 8B C1                        mov rax, rcx
005B8AAB  25 55 03 00 00                  and eax, 0x355
005B8AB0  48 F7 D8                        neg rax
005B8AB3  48 1B C0                        sbb rax, rax
005B8AB6  48 23 C1                        and rax, rcx
005B8AB9  C3                              ret
005B8ABA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiReadKernelDr7(void)
{
    __int64 result;

    result = (unsigned int)((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 328)) & (853));
    result = -(result);
    result = (result) & (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 328));
    return result;
}
```

## 5. (Beta) C Style

```c
void KiReadKernelDr7(void)
{
    int64_t result;

    result = (uint32_t)((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x148)) & (853));
    result = -(result);
    result = (result) & (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x148));
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005B8A98&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005B8A98[BB_005B8A98]
  bb_005B8ABA[BB_005B8ABA]
```
