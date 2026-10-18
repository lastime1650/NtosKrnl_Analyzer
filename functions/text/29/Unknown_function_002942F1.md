# sub_002942F1

- RVA: `0x002942F1`–`0x0029430C` (길이 `27` bytes)
- VA: `0x00000001402942F1`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00067744`
- 디코드: `7`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00294306` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002942F1  4C 8B CF                        mov r9, rdi
002942F4  48 89 6C 24 20                  mov qword ptr [rsp + 0x20], rbp
002942F9  4D 8B C2                        mov r8, r10
002942FC  BA 82 07 00 00                  mov edx, 0x782
00294301  B9 1A 00 00 00                  mov ecx, 0x1a
00294306  E8 55 93 26 00                  call 0x1404fd660
0029430B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_002942F1(void)
{
    __int64 result;
    unsigned __int64 v_stack_p20;

    v_stack_p20 = v_rbp;
    result = KeBugCheckEx(26, (unsigned int)(0x782ULL), v_r10, v_rdi);
    return result;
}
```

## 5. (Beta) C Style

```c
void sub_002942F1(void)
{
    int64_t result;
    uint64_t v_stack_p20;

    v_stack_p20 = local_rbp;
    result = KeBugCheckEx(26, (uint32_t)(0x782ULL), local_r10, local_rdi);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002942F1&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002942F1[BB_002942F1]
```
