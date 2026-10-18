# sub_0091A1C3

- RVA: `0x0091A1C3`–`0x0091A1DB` (길이 `24` bytes)
- VA: `0x000000014091A1C3`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008ADC8`
- 디코드: `9`개 명령, `24/24` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0091A1CB` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0091A1CB` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0091A1C3  BA 50 73 45 6E                  mov edx, 0x6e457350
0091A1C8  48 8B CB                        mov rcx, rbx
0091A1CB  E8 10 D7 9D FF                  call 0x1402f78e0
0091A1D0  48 8B C5                        mov rax, rbp
0091A1D3  48 83 C4 38                     add rsp, 0x38
0091A1D7  5D                              pop rbp
0091A1D8  5B                              pop rbx
0091A1D9  C3                              ret
0091A1DA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0091A1C3(void)
{
    __int64 result;
    __int64 v_rsp;

    result = ObfDereferenceObjectWithTag(v_rbx, (unsigned int)(0x6E457350ULL), a3, a4);
    v_rsp = (v_rsp) + (56);
    return v_rbp;
}
```

## 5. (Beta) C Style

```c
void sub_0091A1C3(void)
{
    int64_t result;
    int64_t local_rsp;

    result = ObfDereferenceObjectWithTag(local_rbx, (uint32_t)(0x6E457350ULL), a3, a4);
    local_rsp = (local_rsp) + (56);
    return local_rbp;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0091A1C3&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0091A1C3[BB_0091A1C3]
  bb_0091A1DA[BB_0091A1DA]
```
