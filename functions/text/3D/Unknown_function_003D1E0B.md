# sub_003D1E0B

- RVA: `0x003D1E0B`–`0x003D1E27` (길이 `28` bytes)
- VA: `0x00000001403D1E0B`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000912D4`
- 디코드: `7`개 명령, `28/28` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003D1E1D` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x003D1E22` → [sub_003D1C93 + 0x103](Unknown_function_003D1C93.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003D1E0B  4D 8B 4D 48                     mov r9, qword ptr [r13 + 0x48]
003D1E0F  4D 8B C7                        mov r8, r15
003D1E12  49 8B 55 28                     mov rdx, qword ptr [r13 + 0x28]
003D1E16  48 8B C5                        mov rax, rbp
003D1E19  49 8B 4D 20                     mov rcx, qword ptr [r13 + 0x20]
003D1E1D  E8 AE 8C 2E 00                  call 0x1406baad0
003D1E22  E9 6F FF FF FF                  jmp 0x1403d1d96
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_003D1E0B(void)
{
    __int64 result;

    result = guard_dispatch_icall(*(unsigned __int64 *)(v_r13 + 32), *(unsigned __int64 *)(v_r13 + 40), v_r15, *(unsigned __int64 *)(v_r13 + 72));
}
```

## 5. (Beta) C Style

```c
void sub_003D1E0B(void)
{
    int64_t result;

    result = guard_dispatch_icall(*(uint64_t *)(local_r13 + 0x20), *(uint64_t *)(local_r13 + 0x28), local_r15, *(uint64_t *)(local_r13 + 0x48));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003D1E0B&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003D1E0B[BB_003D1E0B]
```
