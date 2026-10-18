# sub_006D81CC

- RVA: `0x006D81CC`–`0x006D81E4` (길이 `24` bytes)
- VA: `0x00000001406D81CC`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00062B30`
- 디코드: `7`개 명령, `24/24` bytes 표시
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
  - `0x006D81DF` → [sub_0024A3A0 + 0x2A](../24/Unknown_function_0024A3A0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006D81CC  48 C1 EF 09                     shr rdi, 9
006D81D0  48 23 FA                        and rdi, rdx
006D81D3  49 8B C1                        mov rax, r9
006D81D6  48 03 F8                        add rdi, rax
006D81D9  48 83 E9 01                     sub rcx, 1
006D81DD  75 ED                           jne 0x1406d81cc
006D81DF  E9 E6 21 B7 FF                  jmp 0x14024a3ca
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006D81CC(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 v_rdi;

    v_rdi = (v_rdi) >> (9);
    v_rdi = (v_rdi) & (a2);
    v_rdi = (v_rdi) + (a4);
    a1 = (a1) - (1);
    if (condition_is_not_equal) goto loc_006D81CC;
}
```

## 5. (Beta) C Style

```c
int64_t sub_006D81CC(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t local_rdi;

    local_rdi = (local_rdi) >> (9);
    local_rdi = (local_rdi) & (Arg2);
    local_rdi = (local_rdi) + (Arg4);
    Arg1 = (Arg1) - (1);
    if (condition_is_not_equal) goto loc_006D81CC;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006D81CC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006D81CC[BB_006D81CC]
  bb_006D81DF[BB_006D81DF]
  bb_006D81CC -->|branch| bb_006D81CC
  bb_006D81CC -->|fallthrough| bb_006D81DF
```
