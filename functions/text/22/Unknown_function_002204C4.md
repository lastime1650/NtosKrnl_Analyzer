# sub_002204C4

- RVA: `0x002204C4`–`0x002204DE` (길이 `26` bytes)
- VA: `0x00000001402204C4`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005F38C`
- 디코드: `6`개 명령, `26/26` bytes 표시
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
  - `0x002204D7` → [sub_00220520](Unknown_function_00220520.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002204C4  4C 89 74 24 50                  mov qword ptr [rsp + 0x50], r14
002204C9  45 8B F7                        mov r14d, r15d
002204CC  0F 1F 40 00                     nop dword ptr [rax]
002204D0  F0 48 0F BA 6F 40 00            lock bts qword ptr [rdi + 0x40], 0
002204D7  72 47                           jb 0x140220520
002204D9  4C 8B 74 24 50                  mov r14, qword ptr [rsp + 0x50]
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_002204C4(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10)
{
    unsigned __int64 v_stack_p50;

    v_stack_p50 = v_r14;
    return;
}
```

## 5. (Beta) C Style

```c
void sub_002204C4(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, int64_t Arg10)
{
    uint64_t v_stack_p50;

    v_stack_p50 = local_r14;
    return;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002204C4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002204C4[BB_002204C4]
  bb_002204D9[BB_002204D9]
  bb_002204C4 -->|fallthrough| bb_002204D9
```
