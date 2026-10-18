# RtlExtendedMagicDivide

- RVA: `0x00457BF0`–`0x00457C15` (길이 `37` bytes)
- VA: `0x0000000140457BF0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `14`개 명령, `37/37` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [RtlTimeToSecondsSince1980](RtlTimeToSecondsSince1980_function_00457B70.md) at `0x00457B84`
- [RtlTimeToSecondsSince1970](RtlTimeToSecondsSince1970_function_00457BB0.md) at `0x00457BC4`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00457BF0  4C 8B C9                        mov r9, rcx
00457BF3  48 8B C2                        mov rax, rdx
00457BF6  48 F7 D9                        neg rcx
00457BF9  49 0F 48 C9                     cmovs rcx, r9
00457BFD  48 F7 E1                        mul rcx
00457C00  41 8A C8                        mov cl, r8b
00457C03  48 D3 EA                        shr rdx, cl
00457C06  4D 85 C9                        test r9, r9
00457C09  78 05                           js 0x140457c10
00457C0B  48 8B C2                        mov rax, rdx
00457C0E  C3                              ret
00457C0F  CC                              int3
00457C10  48 F7 DA                        neg rdx
00457C13  EB F6                           jmp 0x140457c0b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlExtendedMagicDivide(__int64 a1, __int64 a2, unsigned __int8 a3)
{
    a1 = -(a1);
    if (sign_flag) { a1 = a1; }
    a2 = (a2) >> (a3);
    if (sign_flag) goto loc_00457C10;
loc_00457C0B:
    return a2;
loc_00457C10:
    a2 = -(a2);
    goto loc_00457C0B;
}
```

## 5. (Beta) C Style

```c
int64_t RtlExtendedMagicDivide(int64_t Arg1, int64_t Arg2, uint8_t Arg3)
{
    Arg1 = -(Arg1);
    if (sign_flag) { Arg1 = Arg1; }
    Arg2 = (Arg2) >> (Arg3);
    if (sign_flag) goto loc_00457C10;
loc_00457C0B:
    return Arg2;
loc_00457C10:
    Arg2 = -(Arg2);
    goto loc_00457C0B;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00457BF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00457BF0[BB_00457BF0]
  bb_00457C0B[BB_00457C0B]
  bb_00457C0F[BB_00457C0F]
  bb_00457C10[BB_00457C10]
  bb_00457BF0 -->|branch| bb_00457C10
  bb_00457BF0 -->|fallthrough| bb_00457C0B
  bb_00457C0F -->|flow| bb_00457C10
  bb_00457C10 -->|branch| bb_00457C0B
```
