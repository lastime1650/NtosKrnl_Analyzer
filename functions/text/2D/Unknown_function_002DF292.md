# sub_002DF292

- RVA: `0x002DF292`–`0x002DF2AD` (길이 `27` bytes)
- VA: `0x00000001402DF292`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000709FC`
- 디코드: `12`개 명령, `27/27` bytes 표시
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
002DF292  48 81 C4 80 00 00 00            add rsp, 0x80
002DF299  41 5F                           pop r15
002DF29B  41 5E                           pop r14
002DF29D  41 5D                           pop r13
002DF29F  41 5C                           pop r12
002DF2A1  5F                              pop rdi
002DF2A2  5E                              pop rsi
002DF2A3  5B                              pop rbx
002DF2A4  C3                              ret
002DF2A5  CC                              int3
002DF2A6  B8 01 00 00 C0                  mov eax, 0xc0000001
002DF2AB  EB E5                           jmp 0x1402df292
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_002DF292(void)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) + (128);
    return result;
}
```

## 5. (Beta) C Style

```c
void sub_002DF292(void)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) + (128);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002DF292&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002DF292[BB_002DF292]
  bb_002DF2A5[BB_002DF2A5]
  bb_002DF2A5 -->|branch| bb_002DF292
```
