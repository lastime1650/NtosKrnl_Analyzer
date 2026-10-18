# SleepstudyHelperSetBlockerVisible

- RVA: `0x007749B0`–`0x007749C1` (길이 `17` bytes)
- VA: `0x00000001407749B0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `7`개 명령, `17/17` bytes 표시
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
007749B0  B8 0D 00 00 C0                  mov eax, 0xc000000d
007749B5  48 85 C9                        test rcx, rcx
007749B8  74 05                           je 0x1407749bf
007749BA  88 51 58                        mov byte ptr [rcx + 0x58], dl
007749BD  33 C0                           xor eax, eax
007749BF  C3                              ret
007749C0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SleepstudyHelperSetBlockerVisible(__int64 a1, unsigned __int8 a2)
{
    __int64 result;

    result = (unsigned int)(0xC000000DULL);
    if (a1 != 0) {
        *(unsigned __int8 *)(a1 + 88) = a2;
        result = 0;
    }
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SleepstudyHelperSetBlockerVisible(int64_t Arg1, uint8_t Arg2)
{
    int64_t result;

    result = (uint32_t)(0xC000000DULL);
    if (Arg1 != 0) {
        *(uint8_t *)(Arg1 + 0x58) = Arg2;
        result = 0;
    }
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007749B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007749B0[BB_007749B0]
  bb_007749BA[BB_007749BA]
  bb_007749BF[BB_007749BF]
  bb_007749C0[BB_007749C0]
  bb_007749B0 -->|branch| bb_007749BF
  bb_007749B0 -->|fallthrough| bb_007749BA
  bb_007749BA -->|flow| bb_007749BF
```
