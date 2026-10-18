# sub_00B1961E

- RVA: `0x00B1961E`–`0x00B1963E` (길이 `32` bytes)
- VA: `0x0000000140B1961E`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007DE64`
- 디코드: `9`개 명령, `32/32` bytes 표시
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
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00B19631` → [AlpcpCreateRegion + 0x9C](../89/AlpcpCreateRegion_function_008933B0.md) (`tail-transfer`)
  - `0x00B19639` → [AlpcpCreateRegion + 0xBE](../89/AlpcpCreateRegion_function_008933B0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B1961E  48 8B D1                        mov rdx, rcx
00B19621  4C 8B C3                        mov r8, rbx
00B19624  4C 8B C8                        mov r9, rax
00B19627  48 8B 59 20                     mov rbx, qword ptr [rcx + 0x20]
00B1962B  48 8B 09                        mov rcx, qword ptr [rcx]
00B1962E  49 03 DA                        add rbx, r10
00B19631  E9 16 9E D7 FF                  jmp 0x14089344c
00B19636  48 8B F9                        mov rdi, rcx
00B19639  E9 30 9E D7 FF                  jmp 0x14089346e
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_00B1961E(__int64 a1)
{
    __int64 v_rbx;

    v_rbx = (*(unsigned __int64 *)(a1 + 32)) + (v_r10);
}
```

## 5. (Beta) C Style

```c
void sub_00B1961E(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t local_rbx;

    local_rbx = (*(uint64_t *)(arg1 + 0x20)) + (local_r10);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B1961E&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B1961E[BB_00B1961E]
  bb_00B19636[BB_00B19636]
```
