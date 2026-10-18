# SANITIZE_DRADDR

- RVA: `0x00443940`–`0x0044395E` (길이 `30` bytes)
- VA: `0x0000000140443940`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `10`개 명령, `30/30` bytes 표시
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
00443940  85 D2                           test edx, edx
00443942  75 05                           jne 0x140443949
00443944  48 8B C1                        mov rax, rcx
00443947  C3                              ret
00443948  CC                              int3
00443949  33 D2                           xor edx, edx
0044394B  48 B8 FF FF FE FF FF 7F 00 00   movabs rax, 0x7ffffffeffff
00443955  48 3B C8                        cmp rcx, rax
00443958  48 0F 47 CA                     cmova rcx, rdx
0044395C  EB E6                           jmp 0x140443944
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SANITIZE_DRADDR(__int64 a1, int a2)
{
    if (a2 != 0) goto loc_00443949;
loc_00443944:
    return a1;
loc_00443949:
    a2 = 0;
    if (a1 > a1) { a1 = 0; }
    goto loc_00443944;
}
```

## 5. (Beta) C Style

```c
int64_t SANITIZE_DRADDR(int64_t Arg1, int32_t Arg2)
{
    if (Arg2 != 0) goto loc_00443949;
loc_00443944:
    return Arg1;
loc_00443949:
    Arg2 = 0;
    if (Arg1 > Arg1) { Arg1 = 0; }
    goto loc_00443944;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00443940&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00443940[BB_00443940]
  bb_00443944[BB_00443944]
  bb_00443948[BB_00443948]
  bb_00443949[BB_00443949]
  bb_00443940 -->|branch| bb_00443949
  bb_00443940 -->|fallthrough| bb_00443944
  bb_00443948 -->|flow| bb_00443949
  bb_00443949 -->|branch| bb_00443944
```
