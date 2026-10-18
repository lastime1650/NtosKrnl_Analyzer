# sub_00984D21

- RVA: `0x00984D21`–`0x00984D37` (길이 `22` bytes)
- VA: `0x0000000140984D21`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00097B98`
- 디코드: `10`개 명령, `22/22` bytes 표시
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
00984D21  B8 F4 00 00 C0                  mov eax, 0xc00000f4
00984D26  48 81 C4 E8 00 00 00            add rsp, 0xe8
00984D2D  41 5E                           pop r14
00984D2F  41 5C                           pop r12
00984D31  5F                              pop rdi
00984D32  5E                              pop rsi
00984D33  5B                              pop rbx
00984D34  5D                              pop rbp
00984D35  C3                              ret
00984D36  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00984D21(void)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) + (232);
    return (unsigned int)(0xC00000F4ULL);
}
```

## 5. (Beta) C Style

```c
void sub_00984D21(void)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) + (232);
    return (uint32_t)(0xC00000F4ULL);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00984D21&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00984D21[BB_00984D21]
  bb_00984D36[BB_00984D36]
```
