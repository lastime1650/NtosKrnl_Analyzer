# RtlAllocateHeap$filt$0

- RVA: `0x006D1E87`–`0x006D1EA5` (길이 `30` bytes)
- VA: `0x00000001406D1E87`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000716E4`
- 디코드: `12`개 명령, `30/30` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006D1E98` → [RtlpHeapFatalExceptionFilter](../5E/RtlpHeapFatalExceptionFilter_function_005E6F4C.md) (function, `0x005E6F4C`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006D1E87  40 55                           push rbp
006D1E89  48 83 EC 30                     sub rsp, 0x30
006D1E8D  48 8B EA                        mov rbp, rdx
006D1E90  48 8B D1                        mov rdx, rcx
006D1E93  48 8B 01                        mov rax, qword ptr [rcx]
006D1E96  8B 08                           mov ecx, dword ptr [rax]
006D1E98  E8 AF 50 F1 FF                  call 0x1405e6f4c
006D1E9D  90                              nop
006D1E9E  48 83 C4 30                     add rsp, 0x30
006D1EA2  5D                              pop rbp
006D1EA3  C3                              ret
006D1EA4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlAllocateHeap_filt_0(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (48);
    result = RtlpHeapFatalExceptionFilter((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1))), a1, a3, a4);
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlAllocateHeap_filt_0(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (48);
    result = RtlpHeapFatalExceptionFilter((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1))), Arg1, a3, a4);
    local_rsp = (local_rsp) + (48);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006D1E87&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006D1E87[BB_006D1E87]
  bb_006D1EA4[BB_006D1EA4]
```
