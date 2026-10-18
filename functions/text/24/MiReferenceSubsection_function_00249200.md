# MiReferenceSubsection

- RVA: `0x00249200`–`0x0024921B` (길이 `27` bytes)
- VA: `0x0000000140249200`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00062714`
- 디코드: `8`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [sub_002BBACF](../2B/Unknown_function_002BBACF.md) at `0x002BBAE3`
- [sub_002BBACF](../2B/Unknown_function_002BBACF.md) at `0x002BBB0B`
- [sub_002BBC22](../2B/Unknown_function_002BBC22.md) at `0x002BBC57`
- [sub_002BBC8B](../2B/Unknown_function_002BBC8B.md) at `0x002BBCC4`
- [sub_002E10F7](../2E/Unknown_function_002E10F7.md) at `0x002E1186`
- [MiFlushAcquire](../49/MiFlushAcquire_function_00495B70.md) at `0x00495BAE`
- [MiFlushAcquire](../49/MiFlushAcquire_function_00495B70.md) at `0x00495BB8`
- [MiUpdateActiveSubsection](../67/MiUpdateActiveSubsection_function_0067F034.md) at `0x0067F088`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00249215` → [sub_002493D7](Unknown_function_002493D7.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00249200  40 55                           push rbp
00249202  57                              push rdi
00249203  48 83 EC 48                     sub rsp, 0x48
00249207  48 83 79 08 00                  cmp qword ptr [rcx + 8], 0
0024920C  44 8B C2                        mov r8d, edx
0024920F  48 8B 29                        mov rbp, qword ptr [rcx]
00249212  48 8B F9                        mov rdi, rcx
00249215  0F 84 BC 01 00 00               je 0x1402493d7
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall MiReferenceSubsection(__int64 a1, int a2)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (72);
}
```

## 5. (Beta) C Style

```c
void MiReferenceSubsection(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t local_rsp;

    local_rsp = (local_rsp) - (72);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00249200&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00249200[BB_00249200]
```
