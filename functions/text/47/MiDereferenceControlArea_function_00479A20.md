# MiDereferenceControlArea

- RVA: `0x00479A20`–`0x00479A4B` (길이 `43` bytes)
- VA: `0x0000000140479A20`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `14`개 명령, `43/43` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **15**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00479A2D` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x00479A3F` → [MiCheckControlArea](../28/MiCheckControlArea_function_002861B0.md) (function, `0x002861B0`)

### Direct callers
- [MiFaultGetFileExtents](MiFaultGetFileExtents_function_00479758.md) at `0x0047982C`
- [MiRefillPurgedExtents](MiRefillPurgedExtents_function_00479988.md) at `0x004799F6`
- [MiFreeAweView](../../page/6F/MiFreeAweView_function_006FE7A4.md) at `0x006FE82D`
- [sub_0088535F](../../page/88/Unknown_function_0088535F.md) at `0x008854CC`
- [sub_008857C1](../../page/88/Unknown_function_008857C1.md) at `0x008858F2`
- [MiDeleteVad](../../page/88/MiDeleteVad_function_00888C80.md) at `0x008890F1`
- [AlpcpCreateView](../../page/88/AlpcpCreateView_function_0088A9B8.md) at `0x0088AEBF`
- [MiUpdateCfgSystemWideBitmapWorker](../../page/8C/MiUpdateCfgSystemWideBitmapWorker_function_008CE650.md) at `0x008CE753`
- [MiMapImageInSystemSpace](../../page/94/MiMapImageInSystemSpace_function_00941DD8.md) at `0x00941FB4`
- [KsepSdbMapToMemory](../../page/95/KsepSdbMapToMemory_function_0095B81C.md) at `0x0095BB79`
- [MiMapViewOfImageSection](../../page/97/MiMapViewOfImageSection_function_0097E92C.md) at `0x0097F745`
- [MiMapViewInSystemSpace](../../page/98/MiMapViewInSystemSpace_function_009824D8.md) at `0x009825CB`
- [NtGetNlsSectionPtr](../../page/A1/NtGetNlsSectionPtr_function_00A195B0.md) at `0x00A19A8E`
- [MiUnloadSystemImage](../../page/AA/MiUnloadSystemImage_function_00AA2FD4.md) at `0x00AA345A`
- [sub_00B2A146](../../page/B2/Unknown_function_00B2A146.md) at `0x00B2A1CF`
- [sub_00B2A146](../../page/B2/Unknown_function_00B2A146.md) at `0x00B2A486`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00479A20  40 53                           push rbx
00479A22  48 83 EC 20                     sub rsp, 0x20
00479A26  48 8B D9                        mov rbx, rcx
00479A29  48 83 C1 48                     add rcx, 0x48
00479A2D  E8 5E EC DC FF                  call 0x140248690
00479A32  48 FF 4B 28                     dec qword ptr [rbx + 0x28]
00479A36  8A D0                           mov dl, al
00479A38  48 FF 4B 30                     dec qword ptr [rbx + 0x30]
00479A3C  48 8B CB                        mov rcx, rbx
00479A3F  E8 6C C7 E0 FF                  call 0x1402861b0
00479A44  48 83 C4 20                     add rsp, 0x20
00479A48  5B                              pop rbx
00479A49  C3                              ret
00479A4A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiDereferenceControlArea(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a1 = (a1) + (72);
    result = ExAcquireSpinLockExclusive(a1, a2, a3, a4);
    result = MiCheckControlArea(a1, (unsigned __int8)(result), a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiDereferenceControlArea(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    Arg1 = (Arg1) + (72);
    result = ExAcquireSpinLockExclusive(Arg1, a2, a3, a4);
    result = MiCheckControlArea(Arg1, (uint8_t)(result), a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x28` | `64` | `R/W` |
| `Arg1` | `+ 0x30` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00479A20&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00479A20[BB_00479A20]
  bb_00479A4A[BB_00479A4A]
```
