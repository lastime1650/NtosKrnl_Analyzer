# FsRtlCheckOplockEx2$fin$0

- RVA: `0x006D2EB0`–`0x006D2EEF` (길이 `63` bytes)
- VA: `0x00000001406D2EB0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000970BC`
- 디코드: `15`개 명령, `63/63` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006D2EDF` → [ExReleaseFastMutexUnsafe](../25/ExReleaseFastMutexUnsafe_function_002503A0.md) (function, `0x002503A0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006D2EB0  40 55                           push rbp
006D2EB2  48 81 EC 80 00 00 00            sub rsp, 0x80
006D2EB9  48 8B EA                        mov rbp, rdx
006D2EBC  80 BD 80 00 00 00 00            cmp byte ptr [rbp + 0x80], 0
006D2EC3  74 20                           je 0x1406d2ee5
006D2EC5  F7 85 C0 00 00 00 00 00 00 20   test dword ptr [rbp + 0xc0], 0x20000000
006D2ECF  75 14                           jne 0x1406d2ee5
006D2ED1  48 8B 8D E8 00 00 00            mov rcx, qword ptr [rbp + 0xe8]
006D2ED8  48 8B 89 98 00 00 00            mov rcx, qword ptr [rcx + 0x98]
006D2EDF  E8 BC D4 B7 FF                  call 0x1402503a0
006D2EE4  90                              nop
006D2EE5  48 81 C4 80 00 00 00            add rsp, 0x80
006D2EEC  5D                              pop rbp
006D2EED  C3                              ret
006D2EEE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FsRtlCheckOplockEx2_fin_0(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (128);
    if ((*(unsigned __int8 *)(a2 + 128)) == 0) goto loc_006D2EE5;
    if (((*(unsigned int *)(a2 + 192)) & (0x20000000ULL)) == 0) {
        a1 = *(unsigned __int64 *)(a2 + 232);
        a1 = *(unsigned __int64 *)(a1 + 152);
        result = ExReleaseFastMutexUnsafe(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (128);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t FsRtlCheckOplockEx2_fin_0(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (128);
    if ((*(uint8_t *)(arg2 + 0x80)) == 0) goto loc_006D2EE5;
    if (((*(uint32_t *)(arg2 + 0xC0)) & (0x20000000ULL)) == 0) {
        Arg1 = *(uint64_t *)(arg2 + 0xE8);
        Arg1 = *(uint64_t *)(Arg1 + 0x98);
        result = ExReleaseFastMutexUnsafe(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (128);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x80` | `8` | `R` |
| `Arg2` | `+ 0xC0` | `32` | `R` |
| `Arg2` | `+ 0xE8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006D2EB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006D2EB0[BB_006D2EB0]
  bb_006D2EC5[BB_006D2EC5]
  bb_006D2ED1[BB_006D2ED1]
  bb_006D2EE5[BB_006D2EE5]
  bb_006D2EEE[BB_006D2EEE]
  bb_006D2EB0 -->|branch| bb_006D2EE5
  bb_006D2EB0 -->|fallthrough| bb_006D2EC5
  bb_006D2EC5 -->|branch| bb_006D2EE5
  bb_006D2EC5 -->|fallthrough| bb_006D2ED1
  bb_006D2ED1 -->|flow| bb_006D2EE5
```
