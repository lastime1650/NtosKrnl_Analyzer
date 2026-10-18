# WdipSemMergeEvents

- RVA: `0x007B0824`–`0x007B0852` (길이 `46` bytes)
- VA: `0x00000001407B0824`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `15`개 명령, `46/46` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [WdipSemAddContextEventToScenario](../7A/WdipSemAddContextEventToScenario_function_007AF338.md) at `0x007AF394`
- [WdipSemAddEndEventToScenario](../7A/WdipSemAddEndEventToScenario_function_007AF3FC.md) at `0x007AF466`
- [WdipSemMergeScenarios](WdipSemMergeScenarios_function_007B0858.md) at `0x007B0882`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007B0824  48 85 C9                        test rcx, rcx
007B0827  74 27                           je 0x1407b0850
007B0829  48 85 D2                        test rdx, rdx
007B082C  74 22                           je 0x1407b0850
007B082E  0F B6 42 12                     movzx eax, byte ptr [rdx + 0x12]
007B0832  44 0F B6 41 12                  movzx r8d, byte ptr [rcx + 0x12]
007B0837  44 3A C0                        cmp r8b, al
007B083A  44 0F 46 C0                     cmovbe r8d, eax
007B083E  44 88 41 12                     mov byte ptr [rcx + 0x12], r8b
007B0842  48 8B 42 18                     mov rax, qword ptr [rdx + 0x18]
007B0846  48 09 41 18                     or qword ptr [rcx + 0x18], rax
007B084A  8B 42 24                        mov eax, dword ptr [rdx + 0x24]
007B084D  09 41 24                        or dword ptr [rcx + 0x24], eax
007B0850  C3                              ret
007B0851  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall WdipSemMergeEvents(__int64 a1, __int64 a2)
{
    __int64 result;

    if (a1 == 0) goto loc_007B0850;
    if (a2 != 0) {
        result = *(unsigned __int8 *)(a2 + 18);
        a3 = *(unsigned __int8 *)(a1 + 18);
        if (((unsigned __int8)(a3)) <= ((unsigned __int8)(result))) { a3 = (unsigned int)(result); }
        *(unsigned __int8 *)(a1 + 18) = (unsigned __int8)(a3);
        result = *(unsigned __int64 *)(a2 + 24);
        result = *(unsigned int *)(a2 + 36);
    }
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t WdipSemMergeEvents(int64_t Arg1, int64_t Arg2)
{
    int64_t result;

    if (Arg1 == 0) goto loc_007B0850;
    if (Arg2 != 0) {
        result = *(uint8_t *)(Arg2 + 0x12);
        a3 = *(uint8_t *)(Arg1 + 0x12);
        if (((uint8_t)(a3)) <= ((uint8_t)(result))) { a3 = (uint32_t)(result); }
        *(uint8_t *)(Arg1 + 0x12) = (uint8_t)(a3);
        result = *(uint64_t *)(Arg2 + 0x18);
        result = *(uint32_t *)(Arg2 + 0x24);
    }
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007B0824&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007B0824[BB_007B0824]
  bb_007B0829[BB_007B0829]
  bb_007B082E[BB_007B082E]
  bb_007B0850[BB_007B0850]
  bb_007B0851[BB_007B0851]
  bb_007B0824 -->|branch| bb_007B0850
  bb_007B0824 -->|fallthrough| bb_007B0829
  bb_007B0829 -->|branch| bb_007B0850
  bb_007B0829 -->|fallthrough| bb_007B082E
  bb_007B082E -->|flow| bb_007B0850
```
