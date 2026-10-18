# _guard_retpoline_jump_hpat

- RVA: `0x00BCE560`–`0x00BCE575` (길이 `21` bytes)
- VA: `0x0000000140BCE560`
- 실행 섹션: `KSCP`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C2128`
- 디코드: `7`개 명령, `21/21` bytes 표시
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
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BCE560  50                              push rax
00BCE561  48 8B 44 24 08                  mov rax, qword ptr [rsp + 8]
00BCE566  48 8B 80 FB 0F 00 00            mov rax, qword ptr [rax + 0xffb]
00BCE56D  48 89 44 24 08                  mov qword ptr [rsp + 8], rax
00BCE572  58                              pop rax
00BCE573  C3                              ret
00BCE574  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall _guard_retpoline_jump_hpat(void)
{
    unsigned __int64 v_stack_p0;

    v_stack_p0 = *(unsigned __int64 *)(v_stack_p0 + 4091);
    return *(unsigned __int64 *)(v_stack_p0 + 4091);
}
```

## 5. (Beta) C Style

```c
void _guard_retpoline_jump_hpat(void)
{
    uint64_t v_stack_p0;

    v_stack_p0 = *(uint64_t *)(v_stack_p0 + 0xFFB);
    return *(uint64_t *)(v_stack_p0 + 0xFFB);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=kscp&rva=0x00BCE560&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BCE560[BB_00BCE560]
  bb_00BCE574[BB_00BCE574]
```
