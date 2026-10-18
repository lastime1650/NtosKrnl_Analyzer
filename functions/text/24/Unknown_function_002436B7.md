# sub_002436B7

- RVA: `0x002436B7`–`0x002436D0` (길이 `25` bytes)
- VA: `0x00000001402436B7`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00061BD0`
- 디코드: `5`개 명령, `25/25` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x002436C5` → [sub_00243750](Unknown_function_00243750.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002436B7  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
002436BC  33 FF                           xor edi, edi
002436BE  F0 48 0F BA 6B 18 3F            lock bts qword ptr [rbx + 0x18], 0x3f
002436C5  0F 82 85 00 00 00               jb 0x140243750
002436CB  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_002436B7(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8)
{
    __int64 v_rdi;
    unsigned __int64 v_stack_p40;

    v_stack_p40 = v_rdi;
    v_rdi = 0;
    return;
}
```

## 5. (Beta) C Style

```c
void sub_002436B7(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, int64_t Arg8)
{
    int64_t local_rdi;
    uint64_t v_stack_p40;

    v_stack_p40 = local_rdi;
    local_rdi = 0;
    return;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002436B7&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002436B7[BB_002436B7]
  bb_002436CB[BB_002436CB]
  bb_002436B7 -->|fallthrough| bb_002436CB
```
