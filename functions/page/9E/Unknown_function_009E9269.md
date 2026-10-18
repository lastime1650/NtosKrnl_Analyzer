# sub_009E9269

- RVA: `0x009E9269`–`0x009E9280` (길이 `23` bytes)
- VA: `0x00000001409E9269`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A4F28`
- 디코드: `4`개 명령, `23/23` bytes 표시
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
  - `0x009E927B` → [EtwpGetTraceGuidInfo + 0x51](EtwpGetTraceGuidInfo_function_009E8BD0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
009E9269  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
009E926D  4C 8B B0 08 05 00 00            mov r14, qword ptr [rax + 0x508]
009E9274  49 81 C6 26 02 00 00            add r14, 0x226
009E927B  E9 A1 F9 FF FF                  jmp 0x1409e8c21
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_009E9269(__int64 a1)
{
    __int64 v_r14;

    v_r14 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 1288)) + (550);
}
```

## 5. (Beta) C Style

```c
int64_t sub_009E9269(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t local_r14;

    local_r14 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x508)) + (550);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009E9269&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009E9269[BB_009E9269]
```
