# sub_002C1DD3

- RVA: `0x002C1DD3`–`0x002C1DF6` (길이 `35` bytes)
- VA: `0x00000001402C1DD3`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006E7C8`
- 디코드: `8`개 명령, `35/35` bytes 표시
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
  - `0x002C1DF1` → [sub_002C1B47 + 0x1A](Unknown_function_002C1B47.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002C1DD3  49 8B CE                        mov rcx, r14
002C1DD6  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
002C1DE0  48 C1 E9 09                     shr rcx, 9
002C1DE4  48 23 C8                        and rcx, rax
002C1DE7  49 8B C0                        mov rax, r8
002C1DEA  48 03 C8                        add rcx, rax
002C1DED  48 89 4F 48                     mov qword ptr [rdi + 0x48], rcx
002C1DF1  E9 6B FD FF FF                  jmp 0x1402c1b61
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_002C1DD3(__int64 a1, __int64 a2, __int64 a3)
{
    a1 = (v_r14) >> (9);
    a1 = (a1) & (result);
    a1 = (a1) + (a3);
    *(unsigned __int64 *)(v_rdi + 72) = a1;
}
```

## 5. (Beta) C Style

```c
int64_t sub_002C1DD3(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    Arg1 = (local_r14) >> (9);
    Arg1 = (Arg1) & (result);
    Arg1 = (Arg1) + (Arg3);
    *(uint64_t *)(local_rdi + 0x48) = Arg1;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002C1DD3&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002C1DD3[BB_002C1DD3]
```
